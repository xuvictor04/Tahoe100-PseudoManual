---
symbol: "PPP3CA"
type: "gene"
col: 6247
ensembl_id: "ENSG00000138814"
name: "protein phosphatase 3 catalytic subunit alpha"
location: "4q24"
module: 97
arm: "+"
pooled_cpm: 286.93
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PPP3CA

*protein phosphatase 3 catalytic subunit alpha* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +10.6, q 2e-23, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.695× (z -7.7, q 1e-11, down in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.719× (z -7.2, q 1e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF7L2]] (+0.61, fdr 1e-05), [[FOXO1]] (+0.59, fdr 1e-05), [[PPARG]] (+0.57, fdr 2e-05); moves opposite to [[CCDC22]] (-0.57, fdr 2e-05), [[KLHL12]] (-0.56, fdr 2e-05), [[ADPRM]] (-0.51, fdr 4e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +10.6 | 2e-23 | 38/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +7.6 | 9e-12 | 35/48 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 7e-11 | 38/49 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +6.9 | 9e-10 | 33/48 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +6.1 | 1e-07 | 32/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 3e-06 | 31/48 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +5.2 | 2e-05 | 30/49 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.002 | 22/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.17 | 13/49 (H4, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -7.7 | 1e-11 | 36/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -7.2 | 1e-10 | 37/48 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -7.2 | 1e-10 | 29/49 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -7.0 | 3e-10 | 31/48 (KATO III, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.742×** | -6.5 | 7e-09 | 34/48 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.571×** | -6.4 | 1e-08 | 38/48 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -6.1 | 9e-08 | 28/49 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -5.8 | 4e-07 | 29/48 (SW48, A-172, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.635×** | -5.2 | 1e-05 | 34/48 (KATO III, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.789×** | -5.2 | 1e-05 | 28/48 (hTERT-HPNE, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.643×** | -5.0 | 2e-05 | 25/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.786×** | -5.0 | 3e-05 | 27/48 (SW48, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.853× | -4.9 | 4e-05 | 21/48 (LoVo, A-172, …) | all doses, flat | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.796×** | -4.8 | 7e-05 | 32/48 (NCI-H460, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.662×** | -4.7 | 9e-05 | 34/48 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -4.7 | 1e-04 | 28/48 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.741×** | -4.7 | 1e-04 | 33/48 (KATO III, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.823×** | -4.3 | 6e-04 | 23/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.691×** | -4.2 | 7e-04 | 28/48 (KATO III, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 93.8 | 7 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change |
| [[HEC-1-A (line)]] | alt | 192 | 7 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.562× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[NCI-H1573 (line)]] | alt | 247 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -14.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.438× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 99.8 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.6) | — |
| [[LoVo (line)]] | wt | 1,456 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -19.9) |
| [[PANC-1 (line)]] | alt | 210 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.604× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 308 | 1 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.20× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0452× (z -47.4) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.554× (z -9.4) |
| [[SW48 (line)]] | wt | 607 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.283× (z -9.7) |
| [[A-172 (line)]] | wt | 248 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -15.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.439× (z -10.6) |
| [[Hs 766T (line)]] | wt | 129 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -12.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 374 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -15.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.9) |
| [[LS 180 (line)]] | wt | 736 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 129 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -8.7) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H2347 (line)]] | alt | 247 | 3 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.00× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.521× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 264 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.345× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 299 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -12.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H1792 (line)]] | alt | 417 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -17.3) |
| [[RKO (line)]] | wt | 74.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 251 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.546× (z -8.7) |
| [[A498 (line)]] | wt | 413 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.583× (z -9.8) |
| [[A549 (line)]] | wt | 287 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -13.4) |
| [[BT-474 (line)]] | alt | 331 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.391× (z -11.3) |
| [[C32 (line)]] | wt | 208 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.67× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 396 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.0) |
| [[HOP62 (line)]] | alt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.3) |
| [[HS-578T (line)]] | alt | 379 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 334 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.55× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -8.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 306 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.544× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 265 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.55× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 220 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.5) |
| [[SW1417 (line)]] | alt | 183 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.55× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 221 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 171 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF7L2]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 | pathway: Beta-catenin independent WNT signaling |
| [[FOXO1]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PPARG]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MBNL1]] | +0.55 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[UTRN]] | +0.55 | +0.50 / +0.63 | both halves | 1e-05 | STRING 576 |
| [[DPY19L1]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 | same gene group |
| [[NAB1]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LRP6]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Signaling by WNT |
| [[RAPGEF2]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 | same gene group |
| [[ITGA6]] | +0.49 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[MPRIP]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[MAML2]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC22]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[KLHL12]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 | pathway: Signaling by WNT |
| [[ADPRM]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[PAAF1]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PPP1R8]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MIR34AHG]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[YJU2B]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[DENR]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[HPS4]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[GLE1]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FAHD2A]] | -0.47 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[ZFPL1]] | -0.47 | -0.31 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises PPP3CA's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without TBC1D8 | 0.012 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[CD55]] | B | CD55 activity raises PPP3CA's level | lines that do not express CD55 (16) vs lines expressing it (34) | 1.64× lower at baseline in the lines without CD55 | 0.019 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[SERPINE2]] | B | SERPINE2 activity raises PPP3CA's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without SERPINE2 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[PSD3]] | B | PSD3 activity raises PPP3CA's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without PSD3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[ADD3]] | B | ADD3 activity raises PPP3CA's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without ADD3 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[ARHGAP26]] | B | ARHGAP26 activity raises PPP3CA's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[LINC02582]] | B | LINC02582 activity raises PPP3CA's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 1.62× lower at baseline in the lines without LINC02582 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[MAML2]] | B | MAML2 activity raises PPP3CA's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without MAML2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[TNIK]] | B | TNIK activity weakens PPP3CA's drug response | lines that do not express TNIK (11) vs lines expressing it (38) | the lines without TNIK respond 1.10× as strongly (z diff -0.08); strongest at Panobinostat 5 µM: 1.63x vs 1.22x (z diff -3.7) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE; target measured in part of the lines; both ways; artifact flags |
| [[TGFBR2]] | B | TGFBR2 activity raises PPP3CA's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without TGFBR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PPP3CA's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PPP3CA's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.3, 47.3); signed map (10.7, 32.8). **Vector** length 126, 40.2% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.5 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +7.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.2 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -7.8 | -6.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | -6.5 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.8 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -6.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 3 catalytic subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:101,023,409-101,348,278 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CNA1, PPP2B; previously CALN, CALNA |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits; MicroRNA protein coding host genes; Calcineurin subunits |
| Reactome | 18 pathways, smallest: Calcineurin activates NFAT; CLEC7A (Dectin-1) induces NFAT activation; DARPP-32 events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08209](https://www.uniprot.org/uniprotkb/Q08209) (Protein phosphatase 3 catalytic subunit alpha):

> Calcium-dependent, calmodulin-stimulated protein phosphatase which plays an essential role in the transduction of intracellular Ca(2+)-mediated signals. Many of the substrates contain a PxIxIT motif and/or a LxVP motif. In response to increased Ca(2+) levels, dephosphorylates and activates phosphatase SSH1 which results in cofilin dephosphorylation. In response to increased Ca(2+) levels following mitochondrial depolarization, dephosphorylates DNM1L inducing DNM1L translocation to the …

**Summary**, from NCBI Gene [5530](https://www.ncbi.nlm.nih.gov/gene/5530):

> Enables several functions, including ATPase binding activity; calmodulin binding activity; and calmodulin-dependent protein phosphatase activity. Involved in several processes, including calcineurin-NFAT signaling cascade; negative regulation of angiotensin-activated signaling pathway; and positive regulation of transcription by RNA polymerase II. Located in cytoplasmic side of plasma membrane; cytosol; and dendritic spine. Part of calcineurin complex. Implicated in developmental and epileptic …

**Accessions** — [HGNC:9314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9314) · Entrez [5530](https://www.ncbi.nlm.nih.gov/gene/5530) · UniProt [Q08209](https://www.uniprot.org/uniprotkb/Q08209) · Ensembl [ENSG00000138814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138814)

## Data

Gene col 6247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6247); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6247]; `tensor/DDL_lfc|DDL_z.npy` [6247]; `embed/gene_vectors.npy` [6247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6247 or target_col == 6247). Every well: [[PPP3CA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP3CA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
