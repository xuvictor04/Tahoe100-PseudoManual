---
symbol: "UBA6"
type: "gene"
col: 414
ensembl_id: "ENSG00000033178"
name: "ubiquitin like modifier activating enzyme 6"
location: "4q13.2"
module: 154
arm: "+"
pooled_cpm: 354.61
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 39
n_dd_up_clean: 10
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# UBA6

*ubiquitin like modifier activating enzyme 6* — 4q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.62× (z +7.0, q 1e-09, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.423× (z -12.0, q 2e-30, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.634× (z -9.3, q 2e-18, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NGLY1]] (+0.76, fdr 7e-06), [[CIB1]] (+0.75, fdr 1e-05), [[ANKRD37]] (+0.72, fdr 1e-05); moves opposite to [[RNF115]] (-0.74, fdr 7e-06), [[ZMYND11]] (-0.70, fdr 3e-05), [[ZFX]] (-0.68, fdr 4e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CREG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.0 | 1e-09 | 39/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.6 | 5e-06 | 33/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.004 | 33/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.007 | 30/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.69×** | +4.0 | 0.007 | 39/48 (CFPAC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.007 | 29/48 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.021 | 29/48 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.021 | 37/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.041 | 38/48 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.049 | 34/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.049 | 25/48 (NCI-H23, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -12.0 | 2e-30 | 44/44 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.472×** | -10.9 | 4e-25 | 48/49 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -9.3 | 2e-18 | 39/49 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -7.0 | 3e-10 | 44/47 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.627×** | -6.8 | 1e-09 | 43/48 (AsPC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.634×** | -6.1 | 9e-08 | 32/45 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.684×** | -5.5 | 3e-06 | 40/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.694×** | -5.3 | 9e-06 | 39/48 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.699×** | -5.2 | 1e-05 | 40/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -4.6 | 2e-04 | 38/48 (SW 900, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.796×** | -4.5 | 3e-04 | 34/49 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.803×** | -4.5 | 4e-04 | 24/48 (Hs 766T, HS-578T, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.738×** | -4.4 | 5e-04 | 26/48 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.769×** | -4.3 | 6e-04 | 36/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.736×** | -4.3 | 7e-04 | 33/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.812×** | -4.3 | 7e-04 | 24/48 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.802×** | -4.1 | 0.002 | 31/48 (AsPC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.003 | 33/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.766×** | -3.9 | 0.003 | 34/48 (KATO III, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.8 | 0.003 | 22/48 (J82, A549, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.833×** | -3.7 | 0.005 | 23/48 (SHP-77, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 839 | 2 (1 ⚠) | 14 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.451× (z -12.0) |
| [[J82 (line)]] | alt | 626 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -19.1) |
| [[LOX-IMVI (line)]] | wt | 457 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 277 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 371 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.469× (z -12.9) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.7) |
| [[HS-578T (line)]] | alt | 356 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 486 | 1 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -15.2) |
| [[SNU-423 (line)]] | alt | 492 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.1) |
| [[HT-29 (line)]] | alt | 211 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +15.7) | — |
| [[LoVo (line)]] | wt | 296 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.570× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 428 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 427 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.05× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -20.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 523 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 267 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -8.6) |
| [[BT-474 (line)]] | alt | 264 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.29× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 526 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -14.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 382 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 262 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -11.0) |
| [[LS 180 (line)]] | wt | 343 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 260 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 315 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -13.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 195 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +13.2) | — |
| [[A-172 (line)]] | wt | 241 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.0) |
| [[A498 (line)]] | wt | 594 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -16.7) |
| [[COLO 205 (line)]] | alt | 204 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +10.7) | — |
| [[H4 (line)]] | wt | 424 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -11.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 417 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 362 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -8.7) |
| [[KATO III (line)]] | alt | 232 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.470× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 263 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.607× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 290 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -15.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 322 | 2 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.04× (z +8.9) | — |
| [[A-427 (line)]] | wt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 313 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 299 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -8.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 388 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.6) |
| [[SHP-77 (line)]] | alt | 266 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.496× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 413 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 288 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 265 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 281 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 327 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 330 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 317 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGLY1]] | +0.76 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[CIB1]] | +0.75 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.72 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.70 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.69 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[TRPT1]] | +0.69 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[DNAJC5]] | +0.68 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.68 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.67 | +0.75 / +0.41 | both halves | 4e-05 |  |
| [[MPG]] | +0.67 | +0.76 / +0.33 | both halves | 1e-04 |  |
| [[YIF1B]] | +0.67 | +0.70 / +0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[GALNT12]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNRF1]] | +0.66 | +0.73 / +0.45 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.74 | -0.73 / -0.67 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZMYND11]] | -0.70 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[ZFX]] | -0.68 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[IQCH-AS1]] | -0.68 | -0.77 / -0.33 | both halves | 1e-04 |  |
| [[POLR3C]] | -0.68 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[TXNRD2]] | -0.66 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[BRD1]] | -0.65 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[FIZ1]] | -0.64 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | -0.64 | -0.65 / -0.26 | both halves | 3e-04 |  |
| [[ZNF644]] | -0.64 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.63 | -0.65 / -0.23 | both halves | 5e-04 |  |
| [[DIS3L]] | -0.63 | -0.69 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREG2]] | B | CREG2 activity raises UBA6's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without CREG2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[STC1]] | B | STC1 activity raises UBA6's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without STC1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[ZNF215]] | B | ZNF215 activity raises UBA6's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without ZNF215 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[IGFBP3]] | B | IGFBP3 activity raises UBA6's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.33× lower at baseline in the lines without IGFBP3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[BACE2]] | B | BACE2 activity raises UBA6's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without BACE2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.1, 2.9); signed map (-4.2, 47.4). **Vector** length 125, 56.1% of its response variance represented; |z| ≥ 3 in 1,773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +9.4 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +9.3 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.1 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.2 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.0 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.4 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.3 | -6.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.9 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like modifier activating enzyme 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.2 — chr4:67,612,652-67,701,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10808; previously UBE1L2 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes |
| Reactome | 8 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Dengue Virus Attachment and Entry; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [A0AVT1](https://www.uniprot.org/uniprotkb/A0AVT1) (Ubiquitin-like modifier-activating enzyme 6):

> Activates ubiquitin by first adenylating its C-terminal glycine residue with ATP, and thereafter linking this residue to the side chain of a cysteine residue in E1, yielding a ubiquitin-E1 thioester and free AMP. Specific for ubiquitin, does not activate ubiquitin-like peptides. Also activates UBD/FAT10 conjugation via adenylation of its C-terminal glycine. Differs from UBE1 in its specificity for substrate E2 charging. Does not charge cell cycle E2s, such as CDC34. Essential for embryonic …

**Summary**, from NCBI Gene [55236](https://www.ncbi.nlm.nih.gov/gene/55236):

> Modification of proteins with ubiquitin (UBB; MIM 191339) or ubiquitin-like proteins controls many signaling networks and requires a ubiquitin-activating enzyme (E1), a ubiquitin conjugating enzyme (E2), and a ubiquitin protein ligase (E3). UBE1L2 is an E1 enzyme that initiates the activation and conjugation of ubiquitin-like proteins (Jin et al., 2007 [PubMed 17597759]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25581) · Entrez [55236](https://www.ncbi.nlm.nih.gov/gene/55236) · UniProt [A0AVT1](https://www.uniprot.org/uniprotkb/A0AVT1) · Ensembl [ENSG00000033178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033178)

## Data

Gene col 414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 414); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 414]; `tensor/DDL_lfc|DDL_z.npy` [414]; `embed/gene_vectors.npy` [414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 414 or target_col == 414). Every well: [[UBA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
