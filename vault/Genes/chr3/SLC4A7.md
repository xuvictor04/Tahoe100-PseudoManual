---
symbol: "SLC4A7"
type: "gene"
col: 418
ensembl_id: "ENSG00000033867"
name: "solute carrier family 4 member 7"
location: "3p24.1"
module: 110
arm: "+"
pooled_cpm: 241.28
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 44
n_dd_up_clean: 8
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# SLC4A7

*solute carrier family 4 member 7* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +12.3, q 9e-32, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (5 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.672× (z -10.0, q 1e-20, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.72, fdr 7e-06), [[DCBLD2]] (+0.69, fdr 7e-06), [[NT5E]] (+0.66, fdr 7e-06); moves opposite to [[TNRC6A]] (-0.58, fdr 1e-05), [[THAP8]] (-0.57, fdr 1e-05), [[FLVCR2]] (-0.56, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02509]] → it (grade B ⚠); 3 go from it, the strongest it → [[PRKCA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +12.3 | 9e-32 | 33/45 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +9.0 | 1e-16 | 36/45 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.7 | 3e-12 | 32/45 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +7.4 | 2e-11 | 34/45 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 2e-11 | 30/45 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +6.8 | 9e-10 | 29/45 (C32, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +5.9 | 3e-07 | 25/45 (C32, SW1417, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +5.8 | 5e-07 | 31/45 (SHP-77, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.5 | 3e-06 | 24/45 (SW1417, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +5.2 | 1e-05 | 25/47 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.28×** | +4.9 | 4e-05 | 22/44 (A549, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +4.6 | 2e-04 | 24/44 (SW 900, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.24×** | +4.5 | 2e-04 | 23/44 (SW480, LoVo, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 23/45 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.21×** | +4.0 | 0.003 | 21/45 (AsPC-1, RPMI-7951, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 19/44 (Panc 03.27, SNU-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 24/45 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.008 | 20/45 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.057 | 14/44 (SW 900, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.058 | 18/45 (AN3 CA, SNU-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.10× | +2.9 | 0.074 | 11/46 (C32, NCI-H1573, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.074 | 15/45 (LOX-IMVI, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.10× | +2.8 | 0.090 | 1/45 (SW 1271) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.672×** | -10.0 | 1e-20 | 36/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.652×** | -8.9 | 1e-16 | 37/46 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.657×** | -8.8 | 4e-16 | 40/45 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.655×** | -8.5 | 2e-15 | 40/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.762×** | -8.0 | 1e-13 | 33/45 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.722×** | -8.0 | 2e-13 | 35/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.685×** | -7.6 | 3e-12 | 31/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.695×** | -7.4 | 7e-12 | 34/46 (NCI-H23, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.423×** | -6.9 | 4e-10 | 35/46 (RKO, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.723×** | -6.8 | 8e-10 | 30/45 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.749×** | -6.0 | 8e-08 | 30/45 (A498, HOP62, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.819×** | -5.9 | 2e-07 | 23/45 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.804×** | -5.9 | 2e-07 | 28/45 (NCI-H23, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.760×** | -5.7 | 4e-07 | 31/45 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.687×** | -5.6 | 8e-07 | 36/45 (C32, NCI-H23, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.759×** | -5.5 | 1e-06 | 27/44 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.795×** | -5.4 | 2e-06 | 26/46 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 985 | 0 | 23 (10 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.401× (z -30.0) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.315× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 474 | 0 | 21 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.376× (z -34.4) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.125× (z -21.4) |
| [[C32 (line)]] | wt | 222 | 4 (2 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +20.4) | [[Binimetinib (drug)]] 5 µM 0.325× (z -12.6) |
| [[SW48 (line)]] | wt | 397 | 1 (1 ⚠) | 10 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.24× (z +8.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.331× (z -11.6) |
| [[A498 (line)]] | wt | 315 | 1 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.8) | [[Triamcinolone (drug)]] 5 µM 0.507× (z -12.1) |
| [[SW480 (line)]] | alt | 229 | 2 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.1) | [[Trametinib (drug)]] 0.5 µM 0.537× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 65.8 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +20.1) | — |
| [[NCI-H2030 (line)]] | alt | 344 | 0 | 6 (2 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.497× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.407× (z -9.0) |
| [[HT-29 (line)]] | alt | 96.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.2) | — |
| [[LoVo (line)]] | wt | 111 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.481× (z -9.7) |
| [[SNU-1 (line)]] | wt | 202 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.22× (z +13.4) | — |
| [[A-172 (line)]] | wt | 214 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.60× (z +11.5) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.06× (z +8.7) | — |
| [[A549 (line)]] | wt | 255 | 0 | 3 | — | [[Triamcinolone (drug)]] 0.5 µM 0.479× (z -8.7) |
| [[HOP62 (line)]] | alt | 309 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +10.7) | [[Adagrasib (drug)]] 0.05 µM 0.578× (z -17.5) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 88.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +16.4) | — |
| [[RKO (line)]] | wt | 383 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.504× (z -12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.131× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 202 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 211 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW1417 (line)]] | alt | 150 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 191 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 548 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.361× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 256 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.485× (z -12.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.504× (z -11.7) |
| [[LS 180 (line)]] | wt | 77.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.493× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 91.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 183 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 175 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.2) | — |
| [[A-427 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 83.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 186 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.14× (z +10.7) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 548 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[AN3 CA (line)]] | alt | 219 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 186 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 271 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 436 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 396 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NT5E]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[TM4SF1]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NEK10]] | +0.64 | +0.57 / +0.72 | both halves | 1e-05 | STRING 803; ⚠ **readthrough risk**: NEK10 lies 3.3 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ACTN1]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 | pathway: RHOD GTPase cycle; STRING 421 |
| [[B4GALT6]] | +0.64 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[IQCJ-SCHIP1]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6A]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[THAP8]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[FLVCR2]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[MRPL44]] | -0.56 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CWC15]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DCAF5]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PSMA6]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EDN2]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[COPS5]] | -0.55 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[RCOR3]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TENT2]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZNF224]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02509]] | B | LINC02509 activity raises SLC4A7's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without LINC02509 | 0.048 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |
| [[PYGL]] | B | PYGL activity raises SLC4A7's level | lines that do not express PYGL (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without PYGL | 0.079 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCA]] | C | SLC4A7 activity lowers PRKCA's level | lines that do not express SLC4A7 (3) vs lines expressing it (47) | 2.56× higher at baseline in the lines without SLC4A7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, CSPG5, NR4A3; maybe low, not absent; its own permutation p |
| [[YES1]] | C | SLC4A7 activity raises YES1's level | lines that do not express SLC4A7 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without SLC4A7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, CSPG5, NR4A3; maybe low, not absent; its own permutation p |
| [[LUCAT1]] | C | SLC4A7 activity lowers LUCAT1's level | lines that do not express SLC4A7 (3) vs lines expressing it (47) | 2.18× higher at baseline in the lines without SLC4A7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, CSPG5, NR4A3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.2, 6.7); signed map (5.8, 45.9). **Vector** length 153, 53.9% of its response variance represented; |z| ≥ 3 in 1,913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +9.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.6 | +5.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.5 | +4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.0 | +7.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.5 | +1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -10.8 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.4 | -10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -8.4 | -8.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.0 | -8.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.9 | -8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.6 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -7.4 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:27,372,723-27,484,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NBC3, SBC2; previously SLC4A6 |
| Gene groups (HGNC) | Solute carrier family 4 |
| Reactome | 12 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; RHOH GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6M7](https://www.uniprot.org/uniprotkb/Q9Y6M7) (Sodium bicarbonate cotransporter 3):

> Electroneutral sodium- and bicarbonate-dependent cotransporter with a Na(+):HCO3(-) 1:1 stoichiometry. Mediates the sodium-dependent bicarbonate transport important for pH recovery after acid load as well as for regulation of steady-state pH in the duodenum and vascular smooth muscle cells (By similarity). Plays a key role in macrophage acidification, mediating bicarbonate import into the cytoplasm which is crucial for net acid extrusion and maintenance of cytoplasmic pH during phagocytosis. …

**Summary**, from NCBI Gene [9497](https://www.ncbi.nlm.nih.gov/gene/9497):

> This locus encodes a sodium bicarbonate cotransporter. The encoded transmembrane protein appears to transport sodium and bicarbonate ions in a 1:1 ratio, and is thus considered an electroneutral cotransporter. The encoded protein likely plays a critical role in regulation of intracellular pH involved in visual and auditory sensory transmission. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:11033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11033) · Entrez [9497](https://www.ncbi.nlm.nih.gov/gene/9497) · UniProt [Q9Y6M7](https://www.uniprot.org/uniprotkb/Q9Y6M7) · Ensembl [ENSG00000033867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033867)

## Data

Gene col 418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 418); `tables/drug_effects.parquet` (96 rows, flagged included); `relations/gene_relations.parquet` (col_a == 418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 418]; `tensor/DDL_lfc|DDL_z.npy` [418]; `embed/gene_vectors.npy` [418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 418 or target_col == 418). Every well: [[SLC4A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
