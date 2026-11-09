---
symbol: "VPS13B"
type: "gene"
col: 5337
ensembl_id: "ENSG00000132549"
name: "vacuolar protein sorting 13 homolog B"
location: "8q22.2"
module: 185
arm: "+"
pooled_cpm: 358.03
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# VPS13B

*vacuolar protein sorting 13 homolog B* — 8q22.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.412× (z -12.6, q 2e-33, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.630× (z -9.6, q 1e-19, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC4]] (+0.71, fdr 1e-05), [[PRH1]] (+0.69, fdr 7e-06), [[SUMF1]] (+0.66, fdr 1e-05); moves opposite to [[CEP295NL]] (-0.54, fdr 1e-05), [[RPS6KA1]] (-0.51, fdr 2e-05), [[ADGRB2]] (-0.49, fdr 4e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 1.49× | +3.1 | 0.41 | 39/50 (NCI-H2347, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.41 | 30/47 (SW48, LS 180, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.49× | +3.1 | 0.41 | 34/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.412×** | -12.6 | 2e-33 | 47/47 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.466×** | -10.8 | 8e-25 | 44/44 (SNU-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -9.6 | 1e-19 | 40/49 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.514×** | -9.1 | 2e-17 | 44/45 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.467×** | -8.5 | 1e-15 | 44/49 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -7.6 | 3e-12 | 44/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.658×** | -6.2 | 6e-08 | 42/48 (NCI-H1573, KATO III, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.621×** | -5.3 | 7e-06 | 45/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.697×** | -5.3 | 7e-06 | 35/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.700×** | -5.2 | 9e-06 | 42/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.699×** | -5.1 | 2e-05 | 41/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.714×** | -4.8 | 9e-05 | 36/48 (H4, SNU-423, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -4.7 | 1e-04 | 34/48 (LOX-IMVI, CHP-212, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.822×** | -4.1 | 0.002 | 24/48 (C32, AN3 CA, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.756×** | -4.0 | 0.003 | 31/50 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.850× | -3.4 | 0.023 | 17/49 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.788×** | -3.2 | 0.035 | 34/47 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.067 | 27/49 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.820×** | -2.9 | 0.093 | 27/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -2.9 | 0.097 | 27/48 (MIA PaCa-2, C-33 A, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 310 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -14.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.4) |
| [[KATO III (line)]] | alt | 283 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -9.7) |
| [[C32 (line)]] | wt | 447 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 407 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -10.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -9.5) |
| [[LoVo (line)]] | wt | 278 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.429× (z -12.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 512 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -14.9) |
| [[SW480 (line)]] | alt | 294 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -12.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.526× (z -8.8) |
| [[A498 (line)]] | wt | 526 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 305 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.336× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 418 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -15.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 452 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -19.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -12.9) |
| [[SNU-423 (line)]] | alt | 239 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.7) |
| [[SW 900 (line)]] | alt | 415 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -13.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.9) |
| [[A-172 (line)]] | wt | 236 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.4) |
| [[A-427 (line)]] | wt | 268 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 427 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.7) |
| [[C-33 A (line)]] | alt | 385 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 267 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -10.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 440 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -17.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 688 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -15.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.2) |
| [[PANC-1 (line)]] | alt | 367 | 0 | 4 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.481× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.9) |
| [[A549 (line)]] | wt | 355 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -17.0) |
| [[RKO (line)]] | wt | 730 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -12.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.5) |
| [[CHP-212 (line)]] | wt | 360 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.5) |
| [[COLO 205 (line)]] | alt | 413 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -12.3) ⚠ toxic |
| [[H4 (line)]] | wt | 334 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.373× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HepG2_C3A (line)]] | wt | 250 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -10.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 427 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -12.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 531 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.395× (z -10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.5) |
| [[HT-29 (line)]] | alt | 257 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.445× (z -9.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.479× (z -9.2) |
| [[LS 180 (line)]] | wt | 270 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 321 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 284 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 344 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 406 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 338 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -12.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 357 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -13.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 371 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Hs 766T (line)]] | wt | 250 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -10.2) ⚠ toxic |
| [[J82 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 356 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -11.7) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -8.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 298 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 451 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 292 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | +0.71 | +0.49 / +0.81 | both halves | 1e-05 |  |
| [[PRH1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SUMF1]] | +0.66 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[COMMD10]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[NSMCE2]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[THADA]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[WDR70]] | +0.63 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SCAPER]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[FAM172A]] | +0.60 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[IFT43]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP295NL]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RPS6KA1]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ADGRB2]] | -0.49 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[AHDC1]] | -0.48 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FOXO6]] | -0.47 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[EML2]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises VPS13B's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.5, 29.5); signed map (-6.0, -20.5). **Vector** length 97.7, 42.7% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Thymol (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.0 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.5 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 13 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:99,013,266-99,877,580 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLTP5B; previously CHS1, COH1 |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7G8](https://www.uniprot.org/uniprotkb/Q7Z7G8) (Intermembrane lipid transfer protein VPS13B):

> Mediates the transfer of lipids between membranes at organelle contact sites (By similarity). Binds phosphatidylinositol 3-phosphate (By similarity). Functions as a tethering factor in the slow endocytic recycling pathway, to assist traffic between early and recycling endosomes. Involved in the transport of proacrosomal vesicles to the nuclear dense lamina (NDL) during spermatid development (By similarity). Plays a role in the assembly of the Golgi apparatus, possibly by mediating trafficking …

**Summary**, from NCBI Gene [157680](https://www.ncbi.nlm.nih.gov/gene/157680):

> This gene encodes a potential transmembrane protein that may function in vesicle-mediated transport and sorting of proteins within the cell. This protein may play a role in the development and the function of the eye, hematological system, and central nervous system. Mutations in this gene have been associated with Cohen syndrome. Multiple splice variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2183) · Entrez [157680](https://www.ncbi.nlm.nih.gov/gene/157680) · UniProt [Q7Z7G8](https://www.uniprot.org/uniprotkb/Q7Z7G8) · Ensembl [ENSG00000132549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132549)

## Data

Gene col 5337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5337); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5337]; `tensor/DDL_lfc|DDL_z.npy` [5337]; `embed/gene_vectors.npy` [5337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5337 or target_col == 5337). Every well: [[VPS13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
