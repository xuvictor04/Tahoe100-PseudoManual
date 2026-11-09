---
symbol: "SMURF2"
type: "gene"
col: 3006
ensembl_id: "ENSG00000108854"
name: "SMAD specific E3 ubiquitin protein ligase 2"
location: "17q23.3-q24.1"
module: 120
arm: "+"
pooled_cpm: 351.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# SMURF2

*SMAD specific E3 ubiquitin protein ligase 2* — 17q23.3-q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.54× (z +8.2, q 1e-13, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -13.6, q 4e-39, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASA2]] (+0.71, fdr 7e-06), [[DLC1]] (+0.69, fdr 7e-06), [[BCAR3]] (+0.68, fdr 7e-06); moves opposite to [[BTN3A3]] (-0.53, fdr 1e-05), [[LINC00278]] (-0.48, fdr 5e-05), [[TOM1]] (-0.48, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +8.2 | 1e-13 | 38/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.9 | 2e-09 | 36/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +6.1 | 3e-07 | 37/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.9 | 4e-07 | 33/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +5.8 | 6e-07 | 32/47 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 6e-07 | 30/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +5.4 | 6e-06 | 27/49 (HT-29, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +5.0 | 4e-05 | 34/49 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +4.4 | 6e-04 | 27/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.003 | 24/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.024 | 25/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.059 | 21/46 (A-172, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.075 | 18/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +3.0 | 0.10 | 18/48 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3006.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -13.6 | 4e-39 | 37/49 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -11.7 | 2e-29 | 37/44 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.562×** | -10.8 | 5e-25 | 40/49 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.669×** | -7.6 | 6e-12 | 41/48 (HEC-1-A, RKO, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.694×** | -6.9 | 7e-10 | 37/48 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -6.6 | 3e-09 | 35/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.713×** | -6.3 | 2e-08 | 34/48 (J82, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.713×** | -6.3 | 2e-08 | 32/48 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.753×** | -6.2 | 3e-08 | 33/48 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.704×** | -6.1 | 6e-08 | 32/45 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.735×** | -5.8 | 4e-07 | 33/48 (HEC-1-A, LOX-IMVI, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.755×** | -5.8 | 4e-07 | 32/49 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.792×** | -5.1 | 2e-05 | 29/48 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.827×** | -4.9 | 4e-05 | 23/49 (HEC-1-A, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -4.8 | 5e-05 | 32/48 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.780×** | -4.7 | 1e-04 | 28/47 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.774×** | -4.6 | 1e-04 | 32/47 (J82, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.787×** | -4.5 | 2e-04 | 32/49 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.788×** | -4.2 | 7e-04 | 28/48 (NCI-H23, CHP-212, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.816×** | -3.8 | 0.003 | 28/48 (J82, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.004 | 23/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 1,110 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -22.3) |
| [[J82 (line)]] | alt | 618 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 566 | 0 | 9 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.585× (z -17.7) ⚠ position not correctable · without an alert: [[Auranofin (drug)]] 5 µM 0.254× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 469 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -12.7) |
| [[A-172 (line)]] | wt | 240 | 5 (2 ⚠) | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.82× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -11.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 436 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -13.2) |
| [[HT-29 (line)]] | alt | 185 | 6 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.11× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 768 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 15.0× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 185 | 6 (2 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 3.73× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 205 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.13× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 761 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.8) |
| [[LoVo (line)]] | wt | 155 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +13.8) | — |
| [[SW 900 (line)]] | alt | 369 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.382× (z -11.6) |
| [[A549 (line)]] | wt | 490 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 288 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.3) |
| [[C32 (line)]] | wt | 238 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.76× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 205 | 1 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.67× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 242 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 441 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -11.9) |
| [[A-427 (line)]] | wt | 757 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 550 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 406 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.26× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 163 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 624 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.7) |
| [[PANC-1 (line)]] | alt | 262 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.29× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.0) |
| [[SW480 (line)]] | alt | 395 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -12.7) |
| [[A498 (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 220 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 292 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 408 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.369× (z -8.5) |
| [[Hs 766T (line)]] | wt | 199 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.06× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 392 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 353 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 265 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.475× (z -9.8) |
| [[SNU-423 (line)]] | alt | 383 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.2) |
| [[SW1417 (line)]] | alt | 474 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.4) |
| [[HCT15 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 428 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 207 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA2]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[DLC1]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[BCAR3]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[ELK3]] | +0.65 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MAPK8]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.63 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[MIR222HG]] | +0.61 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.61 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[UBASH3B]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A3]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[LINC00278]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[TOM1]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SMURF2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[TMEM156]] | B | TMEM156 activity raises SMURF2's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.40× lower at baseline in the lines without TMEM156 | 0.093 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[IGF2BP2]] | C | IGF2BP2 activity raises SMURF2's level | lines that do not express IGF2BP2 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without IGF2BP2 | 0.056 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.3, 7.8); signed map (8.5, 45.2). **Vector** length 131, 48.3% of its response variance represented; |z| ≥ 3 in 1,793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.3 | +5.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.9 | +6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.7 | +5.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.6 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.3 | +3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.1 | +2.2 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -6.1 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.9 | -6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | SMAD specific E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3-q24.1 — chr17:64,542,282-64,662,307 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | C2 domain containing; Nedd4 family E3 ubiquitin protein ligases |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 22 pathways, smallest: Downregulation of TGF-beta receptor signaling; Signaling by BMP; Downregulation of SMAD2/3:SMAD4 transcriptional activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAU4](https://www.uniprot.org/uniprotkb/Q9HAU4) (E3 ubiquitin-protein ligase SMURF2):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Interacts with SMAD7 to trigger SMAD7-mediated transforming growth factor beta/TGF-beta receptor ubiquitin-dependent degradation, thereby down-regulating TGF-beta signaling. In addition, interaction with SMAD7 activates autocatalytic degradation, which is prevented by interaction with AIMP1. Also forms a stable …

**Summary**, from NCBI Gene [64750](https://www.ncbi.nlm.nih.gov/gene/64750):

> Enables SMAD binding activity; identical protein binding activity; and ubiquitin protein ligase activity. Involved in several processes, including negative regulation of transforming growth factor beta receptor signaling pathway; positive regulation of ferroptosis; and positive regulation of trophoblast cell migration. Located in nuclear speck. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16809) · Entrez [64750](https://www.ncbi.nlm.nih.gov/gene/64750) · UniProt [Q9HAU4](https://www.uniprot.org/uniprotkb/Q9HAU4) · Ensembl [ENSG00000108854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108854)

## Data

Gene col 3006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3006); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3006]; `tensor/DDL_lfc|DDL_z.npy` [3006]; `embed/gene_vectors.npy` [3006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3006 or target_col == 3006). Every well: [[SMURF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMURF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
