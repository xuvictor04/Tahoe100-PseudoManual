---
symbol: "NEBL"
type: "gene"
col: 1209
ensembl_id: "ENSG00000078114"
name: "nebulette"
location: "10p12.31"
module: 106
arm: "+"
pooled_cpm: 190.02
n_lines_expressing: 33
n_dd_up: 33
n_dd_down: 32
n_dd_up_clean: 32
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 12
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# NEBL

*nebulette* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.56× (z +6.6, q 1e-08, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (19 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.411× (z -13.6, q 3e-39, down in 27 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.494× (z -10.8, q 5e-25, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP2]] (+0.57, fdr 1e-05), [[PLEKHA7]] (+0.57, fdr 1e-05), [[GCLC]] (+0.56, fdr 3e-05); moves opposite to [[SPOCD1]] (-0.49, fdr 3e-05), [[ANTXR2]] (-0.48, fdr 3e-05), [[ADAM19]] (-0.48, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NR5A2]] → it (grade B ⚠); 12 go from it, the strongest it → [[ZBTB7B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +6.6 | 1e-08 | 23/31 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.6 | 1e-08 | 20/31 (J82, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +5.8 | 2e-06 | 22/33 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 8e-06 | 19/32 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.3 | 2e-05 | 21/31 (A-172, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 2e-05 | 17/31 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 2e-05 | 20/31 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.8 | 1e-04 | 19/31 (A-172, J82, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 1e-04 | 18/32 (NCI-H1573, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 19/31 (NCI-H1573, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 18/31 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.74×** | +4.4 | 4e-04 | 19/33 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 8e-04 | 19/31 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 16/32 (SW480, SHP-77, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 0.001 | 19/31 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.001 | 15/31 (A-172, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 21 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.411×** | -13.6 | 3e-39 | 27/31 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.430×** | -12.9 | 1e-35 | 26/31 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.423×** | -12.6 | 2e-34 | 28/31 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -10.8 | 5e-25 | 25/31 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.539×** | -9.5 | 4e-19 | 23/31 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.573×** | -8.2 | 3e-14 | 22/30 (C-33 A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.623×** | -7.0 | 3e-10 | 20/31 (NCI-H2030, A-427, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.630×** | -6.5 | 4e-09 | 23/30 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.661×** | -6.3 | 1e-08 | 24/31 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.628×** | -6.3 | 1e-08 | 24/32 (C-33 A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -6.2 | 3e-08 | 23/31 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -6.1 | 6e-08 | 17/31 (C-33 A, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.475×** | -6.0 | 1e-07 | 23/32 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.712×** | -5.2 | 9e-06 | 20/31 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -4.7 | 1e-04 | 20/31 (A549, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.600×** | -4.1 | 0.001 | 18/31 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.765×** | -4.1 | 0.001 | 21/31 (CHP-212, A549, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.773×** | -3.9 | 0.002 | 16/31 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.005 | 19/31 (A549, PANC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.719×** | -3.6 | 0.007 | 17/31 (Panc 03.27, PANC-1, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.011 | 9/32 (C-33 A, HCT15, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.657×** | -3.4 | 0.015 | 16/31 (SW480, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.858× | -3.3 | 0.017 | 16/32 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.022 | 13/31 (C-33 A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.041 | 12/31 (HT-29, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 172 | 18 (1 ⚠) | 5 (4 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.54× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.305× (z -11.0) |
| [[A-172 (line)]] | wt | 66.9 | 19 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 6.25× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.353× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 679 | 0 | 16 (14 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.125× (z -14.3) |
| [[C-33 A (line)]] | alt | 1,543 | 0 | 16 (14 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.498× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 152 | 5 | 8 (6 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.92× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.298× (z -10.9) |
| [[SHP-77 (line)]] | alt | 162 | 11 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.67× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 445 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.280× (z -10.5) |
| [[SNU-1 (line)]] | wt | 154 | 1 | 9 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.58× (z +8.6) | [[5-Azacytidine (drug)]] 5 µM 0.190× (z -10.6) |
| [[SW480 (line)]] | alt | 391 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -17.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.257× (z -10.0) |
| [[A549 (line)]] | wt | 143 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.321× (z -11.2) |
| [[HT-29 (line)]] | alt | 254 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -17.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.364× (z -9.8) |
| [[J82 (line)]] | alt | 52.9 | 8 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.98× (z +11.5) | — |
| [[LoVo (line)]] | wt | 324 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.464× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 140 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.359× (z -9.5) |
| [[SW 900 (line)]] | alt | 101 | 7 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.29× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.360× (z -8.5) |
| [[PANC-1 (line)]] | alt | 165 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.441× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 120 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.229× (z -13.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 607 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.309× (z -10.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 657 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -11.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.227× (z -12.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 373 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Hs 766T (line)]] | wt | 151 | 1 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.13× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -9.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 390 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 383 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -10.0) ⚠ cell-cycle shift, explains ~88% of this change |
| [[NCI-H2347 (line)]] | alt | 123 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 2.82× (z +9.2) | — |
| [[SW48 (line)]] | wt | 227 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A498 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 44.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 477 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 42.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 24.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2]] | +0.57 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHA7]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GCLC]] | +0.56 | +0.45 / +0.66 | both halves | 3e-05 | **novel candidate** |
| [[CCDC6]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NFIA]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ZFHX3]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SGPP2]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.51 | +0.43 / +0.47 | both halves | 4e-05 | same gene group |
| [[ATF6]] | +0.50 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[HOPX]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[JDP2]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOCD1]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ANTXR2]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ADAM19]] | -0.48 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[VEGFC]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RAI14]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A51]] | -0.45 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[IL33]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SIGLEC15]] | -0.45 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[TMEM132A]] | -0.44 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[SEMA5A]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[ITGA2]] | -0.42 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[HMGN2P46]] | -0.42 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR5A2]] | B | NR5A2 activity strengthens NEBL's drug response | lines that do not express NR5A2 (19) vs lines expressing it (12) | the lines without NR5A2 respond 0.59× as strongly (z diff +2.31); strongest at Ouabain (Octahydrate) 5 µM: 0.58x vs 0.30x (z diff +5.0) | 0.059 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; target measured in part of the lines; artifact flags |
| [[TMTC1]] | B | TMTC1 activity lowers NEBL's level | lines that do not express TMTC1 (25) vs lines expressing it (25) | 1.82× higher at baseline in the lines without TMTC1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000255983, CNRIP1, ADAM23 |
| [[TMEM158]] | B | TMEM158 activity lowers NEBL's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.92× higher at baseline in the lines without TMEM158 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[NR3C1]] | B | NR3C1 activity raises NEBL's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[FGD4]] | B | FGD4 activity raises NEBL's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without FGD4 | 0.089 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SHROOM3]] | C | SHROOM3 activity raises NEBL's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 3.50× lower at baseline in the lines without SHROOM3 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBTB7B]] | B | NEBL activity raises ZBTB7B's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without NEBL | 0.022 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[ANTXR2]] | B | NEBL activity lowers ANTXR2's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.76× higher at baseline in the lines without NEBL | 0.054 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[CCDC6]] | B | NEBL activity raises CCDC6's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without NEBL | 0.056 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[TSHZ3-AS1]] | B | NEBL activity lowers TSHZ3-AS1's level | lines that do not express NEBL (17) vs lines expressing it (33) | 2.39× higher at baseline in the lines without NEBL | 0.067 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[FRMD4A]] | B | NEBL activity lowers FRMD4A's level | lines that do not express NEBL (17) vs lines expressing it (33) | 4.49× higher at baseline in the lines without NEBL | 0.081 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[ATF6]] | B | NEBL activity raises ATF6's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without NEBL | 0.083 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| cells under [[Penfluridol (drug)]] 5 µM | B | NEBL activity raises the cells' numbers under Penfluridol 5 µM (protects the cells) | lines that do not express NEBL (17) vs lines expressing it (31) | the lines without NEBL: 0.86× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[SPOCD1]] | B | NEBL activity lowers SPOCD1's level | lines that do not express NEBL (17) vs lines expressing it (33) | 2.71× higher at baseline in the lines without NEBL | 0.086 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[APCDD1L]] | B | NEBL activity lowers APCDD1L's level | lines that do not express NEBL (17) vs lines expressing it (33) | 2.79× higher at baseline in the lines without NEBL | 0.089 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| cells under [[vincristine (drug)]] 0.5 µM | B | NEBL activity raises the cells' numbers under vincristine 0.5 µM (protects the cells) | lines that do not express NEBL (17) vs lines expressing it (31) | the lines without NEBL: 0.91× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| cells under [[vincristine (drug)]] 5 µM | B | NEBL activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express NEBL (17) vs lines expressing it (31) | the lines without NEBL: 0.75× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[SHROOM3]] | C | NEBL activity raises SHROOM3's level | lines that do not express NEBL (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without NEBL | 0.085 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656; co-absent with the target |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.6, 46.0); signed map (53.7, -10.3). **Vector** length 108, 31.9% of its response variance represented; |z| ≥ 3 in 1,525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.8 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +4.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.9 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.5 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.3 | -3.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -4.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nebulette |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:20,779,973-21,293,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LASP2, LNEBL, bA165O3.1; previously C10orf113 |
| Gene groups (HGNC) | LIM domain containing; Nebulin family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O76041](https://www.uniprot.org/uniprotkb/O76041) (Nebulette):

> Binds to actin and plays an important role in the assembly of the Z-disk. May functionally link sarcomeric actin to the desmin intermediate filaments in the heart muscle sarcomeres.; [Isoform 2]: May play a role in the assembly of focal adhesions.

**Summary**, from NCBI Gene [10529](https://www.ncbi.nlm.nih.gov/gene/10529):

> This gene encodes a nebulin like protein that is abundantly expressed in cardiac muscle. The encoded protein binds actin and interacts with thin filaments and Z-line associated proteins in striated muscle. This protein may be involved in cardiac myofibril assembly. A shorter isoform of this protein termed LIM nebulette is expressed in non-muscle cells and may function as a component of focal adhesion complexes. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar …

**Accessions** — [HGNC:16932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16932) · Entrez [10529](https://www.ncbi.nlm.nih.gov/gene/10529) · UniProt [O76041](https://www.uniprot.org/uniprotkb/O76041) · Ensembl [ENSG00000078114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078114)

## Data

Gene col 1209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1209); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1209]; `tensor/DDL_lfc|DDL_z.npy` [1209]; `embed/gene_vectors.npy` [1209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1209 or target_col == 1209). Every well: [[NEBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
