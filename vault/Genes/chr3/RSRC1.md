---
symbol: "RSRC1"
type: "gene"
col: 10537
ensembl_id: "ENSG00000174891"
name: "arginine and serine rich coiled-coil 1"
location: "3q25.32"
module: 185
arm: "+"
pooled_cpm: 234.51
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# RSRC1

*arginine and serine rich coiled-coil 1* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 1.19× (z +5.3, q 9e-05, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 2 lines (LOX-IMVI 2.05×, SW48 2.11×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 1.72×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.409× (z -39.2, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPIDR]] (+0.65, fdr 7e-06), [[IPO11]] (+0.63, fdr 7e-06), [[VWA8]] (+0.63, fdr 1e-05); moves opposite to [[ZNF440]] (-0.53, fdr 6e-05), [[KCTD11]] (-0.51, fdr 5e-05), [[HELQ]] (-0.51, fdr 2e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AKR1C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10537.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 2 lines (LOX-IMVI 2.05×, SW48 2.11×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 1.72×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +5.3 | 9e-05 | 19/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +5.1 | 9e-05 | 23/48 (HOP62, H4, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +5.0 | 1e-04 | 36/50 (SNU-423, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.18× | +4.9 | 2e-04 | 20/50 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +4.7 | 2e-04 | 17/47 (NCI-H2347, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +4.2 | 0.002 | 17/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +4.1 | 0.003 | 8/49 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.9 | 0.006 | 10/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.006 | 22/49 (NCI-H1573, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.10× | +3.6 | 0.013 | 7/48 (AsPC-1, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.013 | 13/48 (HepG2/C3A, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.12× | +3.6 | 0.013 | 8/49 (AsPC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.6 | 0.016 | 17/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.12× | +3.5 | 0.021 | 15/48 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.12× | +3.4 | 0.021 | 7/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.068 | 6/47 (A498, AsPC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.077 | 8/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.409×** | -39.2 | 0e+00 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -22.1 | 0e+00 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.533×** | -18.8 | 0e+00 | 47/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -17.7 | 0e+00 | 41/49 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -16.9 | 0e+00 | 42/48 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.700×** | -11.1 | 2e-26 | 39/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -10.8 | 3e-25 | 44/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -9.8 | 1e-20 | 37/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.764×** | -8.3 | 5e-15 | 28/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -7.6 | 2e-12 | 27/49 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.800×** | -6.9 | 3e-10 | 26/48 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.808×** | -6.6 | 2e-09 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.802×** | -6.6 | 2e-09 | 25/50 (SW480, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.809×** | -6.6 | 2e-09 | 28/48 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.817×** | -6.2 | 2e-08 | 25/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -6.2 | 2e-08 | 25/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.878× | -5.7 | 4e-07 | 18/48 (SNU-1, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -5.2 | 7e-06 | 20/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.902× | -4.5 | 2e-04 | 2/49 (HOP62, MIA PaCa-2) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.840× | -3.9 | 0.003 | 16/48 (SNU-423, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.842× | -3.8 | 0.003 | 21/48 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.851× | -3.6 | 0.008 | 15/48 (AN3 CA, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 304 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -30.9) |
| [[NCI-H460 (line)]] | wt | 174 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -26.8) |
| [[SW480 (line)]] | alt | 277 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -22.7) |
| [[Panc 03.27 (line)]] | alt | 402 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -23.5) |
| [[A-427 (line)]] | wt | 426 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 283 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -25.0) |
| [[SNU-1 (line)]] | wt | 262 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -16.7) |
| [[SW48 (line)]] | wt | 304 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.11× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.3) |
| [[A498 (line)]] | wt | 250 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -28.3) |
| [[AsPC-1 (line)]] | alt | 110 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -22.8) |
| [[MIA PaCa-2 (line)]] | alt | 307 | 0 | 7 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.324× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 326 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 210 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -20.8) |
| [[HT-29 (line)]] | alt | 169 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -31.4) |
| [[LOX-IMVI (line)]] | wt | 241 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.05× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -22.7) |
| [[NCI-H1573 (line)]] | alt | 220 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.72× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -32.1) |
| [[NCI-H2030 (line)]] | alt | 179 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -22.0) |
| [[SW1417 (line)]] | alt | 270 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -24.6) |
| [[A-172 (line)]] | wt | 243 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -20.2) |
| [[A549 (line)]] | wt | 212 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -21.7) |
| [[BT-474 (line)]] | alt | 294 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -15.8) |
| [[HCT15 (line)]] | alt | 208 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -18.9) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -22.3) |
| [[PANC-1 (line)]] | alt | 263 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -33.9) |
| [[SK-MEL-2 (line)]] | alt | 291 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -17.5) |
| [[SNU-423 (line)]] | alt | 219 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -29.8) |
| [[AN3 CA (line)]] | alt | 379 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -18.4) |
| [[C32 (line)]] | wt | 247 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -18.5) |
| [[Hs 766T (line)]] | wt | 121 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -18.2) |
| [[HS-578T (line)]] | alt | 299 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -13.7) |
| [[KATO III (line)]] | alt | 253 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -19.0) |
| [[LoVo (line)]] | wt | 243 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -28.9) |
| [[LS 180 (line)]] | wt | 222 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -15.4) |
| [[SW 900 (line)]] | alt | 185 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -20.0) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -25.2) |
| [[COLO 205 (line)]] | alt | 230 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -20.3) |
| [[HOP62 (line)]] | alt | 167 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -29.4) |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -16.5) |
| [[H4 (line)]] | wt | 245 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -20.8) |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -17.1) |
| [[RKO (line)]] | wt | 236 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -13.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 217 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.417× (z -12.4) |
| [[SHP-77 (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.540× (z -8.8) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 153 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.163× (z -8.5) |
| [[SW 1271 (line)]] | alt | 327 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.1) |
| [[C-33 A (line)]] | alt | 182 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIDR]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[IPO11]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[VWA8]] | +0.63 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[HERC2]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[CDKAL1]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.62 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[PHKB]] | +0.61 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[PDS5A]] | +0.61 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[SPATA5]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[FTO]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CLASP1]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[USP14]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF440]] | -0.53 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[KCTD11]] | -0.51 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[HELQ]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[SERTAD1]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[C14orf119]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[LINS1]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MCL1]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[KDM6B]] | -0.49 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[ZNF264]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZSWIM3]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[BCAR1]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C1]] | B | AKR1C1 activity lowers RSRC1's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.35× higher at baseline in the lines without AKR1C1 | 0.032 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[PIK3CB]] | B | PIK3CB activity lowers RSRC1's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PIK3CA]] | B | PIK3CA activity lowers RSRC1's level | compounds that target PIK3CA: 2 of 4 raise it (Bimiralisib, GSK1059615) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, -32.3); signed map (-15.3, -49.9). **Vector** length 130, 42.7% of its response variance represented; |z| ≥ 3 in 1,413 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +7.7 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.1 | +3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | +5.9 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.9 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.5 | -18.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -17.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -39.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -22.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | arginine and serine rich coiled-coil 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,105,855-158,545,730 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12197, BM-011, SRrp53, SFRS21 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IZ7](https://www.uniprot.org/uniprotkb/Q96IZ7) (Serine/Arginine-related protein 53):

> Has a role in alternative splicing and transcription regulation. Involved in both constitutive and alternative pre-mRNA splicing. May have a role in the recognition of the 3' splice site during the second step of splicing.

**Summary**, from NCBI Gene [51319](https://www.ncbi.nlm.nih.gov/gene/51319):

> This gene encodes a member of the serine and arginine rich-related protein family. The encoded protein is involved in both constitutive and alternative mRNA splicing. This gene may be associated with schizophrenia. A pseudogene of this gene is located on chromosome 9. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:24152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24152) · Entrez [51319](https://www.ncbi.nlm.nih.gov/gene/51319) · UniProt [Q96IZ7](https://www.uniprot.org/uniprotkb/Q96IZ7) · Ensembl [ENSG00000174891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174891)

## Data

Gene col 10537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10537); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10537]; `tensor/DDL_lfc|DDL_z.npy` [10537]; `embed/gene_vectors.npy` [10537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10537 or target_col == 10537). Every well: [[RSRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
