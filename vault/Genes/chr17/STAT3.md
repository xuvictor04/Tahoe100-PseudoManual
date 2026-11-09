---
symbol: "STAT3"
type: "gene"
col: 9674
ensembl_id: "ENSG00000168610"
name: "signal transducer and activator of transcription 3"
location: "17q21.2"
module: 139
arm: "+"
pooled_cpm: 270.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# STAT3

*signal transducer and activator of transcription 3* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.64× (z +11.0, q 2e-25, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.686× (z -11.8, q 2e-29, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL6]] (+0.64, fdr 7e-06), [[STOM]] (+0.63, fdr 1e-05), [[C3]] (+0.60, fdr 3e-05); moves opposite to [[WNT3]] (-0.47, fdr 2e-04), [[DOK1]] (-0.44, fdr 6e-05), [[GPATCH2]] (-0.44, fdr 1e-04).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HLA-DRB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +11.0 | 2e-25 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +8.0 | 3e-13 | 32/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +6.6 | 1e-08 | 32/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.8 | 9e-07 | 22/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +5.8 | 9e-07 | 33/49 (SNU-1, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.002 | 22/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.0 | 0.005 | 22/48 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.017 | 20/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.017 | 24/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.017 | 19/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.17× | +3.3 | 0.042 | 20/50 (CFPAC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.067 | 18/49 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.686×** | -11.8 | 2e-29 | 44/49 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -10.2 | 7e-22 | 42/48 (C32, LoVo, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.733×** | -9.7 | 4e-20 | 35/49 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.690×** | -7.8 | 1e-12 | 35/48 (C32, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -7.6 | 3e-12 | 33/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.560×** | -6.7 | 2e-09 | 43/48 (SK-MEL-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.749×** | -6.4 | 1e-08 | 37/48 (COLO 205, HT-29, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.586×** | -6.2 | 4e-08 | 38/47 (CFPAC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.765×** | -5.9 | 2e-07 | 31/48 (NCI-H23, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.629×** | -5.4 | 4e-06 | 27/45 (AsPC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.789×** | -5.3 | 8e-06 | 27/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.792×** | -5.2 | 1e-05 | 32/48 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.802×** | -4.9 | 5e-05 | 28/49 (LoVo, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.811×** | -4.6 | 1e-04 | 26/48 (LOX-IMVI, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.826×** | -4.2 | 8e-04 | 25/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.824×** | -4.1 | 0.001 | 25/47 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.003 | 26/48 (SW 900, AsPC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.884× | -3.8 | 0.004 | 15/49 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 372 | 0 | 9 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.420× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 378 | 2 | 7 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.18× (z +9.1) | [[Tofacitinib (drug)]] 5 µM 0.492× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 6 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.462× (z -15.3) |
| [[SW1417 (line)]] | alt | 189 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +11.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.501× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~20% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.656× (z -8.5) |
| [[A-427 (line)]] | wt | 269 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.557× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 463 | 1 | 4 (1 ⚠) | [[Binimetinib (drug)]] 0.05 µM 1.77× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.463× (z -11.8) |
| [[COLO 205 (line)]] | alt | 445 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -13.0) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.442× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 285 | 4 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.78× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.560× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 255 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -12.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.454× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 357 | 3 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.646× (z -8.6) |
| [[SHP-77 (line)]] | alt | 258 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -9.9) |
| [[SW480 (line)]] | alt | 130 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +17.5) | — |
| [[C-33 A (line)]] | alt | 236 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.297× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 154 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.19× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 161 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +13.6) | — |
| [[A498 (line)]] | wt | 380 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.532× (z -8.6) |
| [[BT-474 (line)]] | alt | 270 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -9.4) |
| [[KATO III (line)]] | alt | 238 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +15.6) | — |
| [[LoVo (line)]] | wt | 212 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.345× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 250 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -11.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.506× (z -8.8) |
| [[LS 180 (line)]] | wt | 153 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.83× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 253 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -13.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.428× (z -10.5) |
| [[SNU-423 (line)]] | alt | 332 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -11.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.459× (z -10.9) |
| [[SW 900 (line)]] | alt | 234 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -11.6) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.585× (z -8.8) |
| [[A-172 (line)]] | wt | 249 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.13× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 216 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.527× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 675 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -17.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 285 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.540× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 353 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.545× (z -10.1) |
| [[CHP-212 (line)]] | wt | 477 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.445× (z -10.0) |
| [[H4 (line)]] | wt | 198 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 207 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 215 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.484× (z -8.8) |
| [[HT-29 (line)]] | alt | 240 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.443× (z -10.0) |
| [[J82 (line)]] | alt | 249 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[RPMI-7951 (line)]] | alt | 229 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.91× (z +8.6) | — |
| [[A549 (line)]] | wt | 337 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 231 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 198 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 284 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 243 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 389 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL6]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 903 |
| [[STOM]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[C3]] | +0.60 | +0.46 / +0.62 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[SAA2]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[IFITM2]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 506 |
| [[NAMPT]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 493 |
| [[SAA2-SAA4]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[FGG]] | +0.54 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[ABCA7]] | +0.54 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[SAA4]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LPCAT3]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SUSD6]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT3]] | -0.47 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[DOK1]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 | pathway: Signaling by Non-Receptor Tyrosine Kinases |
| [[GPATCH2]] | -0.44 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[HERC2P9-1]] | -0.43 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[IGHMBP2]] | -0.43 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[TIRAP]] | -0.43 | -0.32 / -0.44 | both halves | 2e-04 | STRING 422 |
| [[BICD1]] | -0.42 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[TRAPPC12]] | -0.42 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[SH3D19]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[L3HYPDH]] | -0.40 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[FBXO30]] | -0.40 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.40 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises STAT3's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.37× lower at baseline in the lines without HLA-DRB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[FGA]] | B | FGA activity raises STAT3's level | lines that do not express FGA (43) vs lines expressing it (7) | 1.48× lower at baseline in the lines without FGA | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[FGB]] | B | FGB activity raises STAT3's level | lines that do not express FGB (42) vs lines expressing it (8) | 1.43× lower at baseline in the lines without FGB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers STAT3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers STAT3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 16.4); signed map (17.1, 28.4). **Vector** length 147, 50.4% of its response variance represented; |z| ≥ 3 in 1,778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +11.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.6 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +6.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -10.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.4 | -6.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -7.0 | -11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.9 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.6 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,313,324-42,388,568 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APRF |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 82 pathways, smallest: MET activates STAT3; Signalling to STAT3; PTK6 Activates STAT3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P40763](https://www.uniprot.org/uniprotkb/P40763) (Signal transducer and activator of transcription 3):

> Signal transducer and transcription activator that mediates cellular responses to interleukins, KITLG/SCF, LEP and other growth factors. Once activated, recruits coactivators, such as NCOA1 or MED1, to the promoter region of the target gene. May mediate cellular responses to activated FGFR1, FGFR2, FGFR3 and FGFR4. Upon activation of IL6ST/gp130 signaling by interleukin-6 (IL6), binds to the IL6-responsive elements identified in the promoters of various acute-phase protein genes. Activated by …

**Summary**, from NCBI Gene [6774](https://www.ncbi.nlm.nih.gov/gene/6774):

> The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein is activated through phosphorylation in response to various cytokines and growth factors including IFNs, EGF, IL5, IL6, HGF, LIF and BMP2. This protein mediates the expression …

**Accessions** — [HGNC:11364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11364) · Entrez [6774](https://www.ncbi.nlm.nih.gov/gene/6774) · UniProt [P40763](https://www.uniprot.org/uniprotkb/P40763) · Ensembl [ENSG00000168610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168610)

## Data

Gene col 9674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9674); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9674]; `tensor/DDL_lfc|DDL_z.npy` [9674]; `embed/gene_vectors.npy` [9674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9674 or target_col == 9674). Every well: [[STAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
