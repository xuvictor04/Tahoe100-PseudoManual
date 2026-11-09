---
symbol: "PRKRIP1"
type: "gene"
col: 4891
ensembl_id: "ENSG00000128563"
name: "PRKR interacting protein 1"
location: "7q22.1"
module: 105
arm: "+"
pooled_cpm: 215.37
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# PRKRIP1

*PRKR interacting protein 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.97× (z +6.7, q 9e-09, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.340× (z -20.5, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -14.6, q 1e-45, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35E1]] (+0.84, fdr 7e-06), [[POM121C]] (+0.82, fdr 7e-06), [[POM121]] (+0.80, fdr 7e-06); moves opposite to [[GMFB]] (-0.64, fdr 1e-05), [[SGPL1]] (-0.62, fdr 3e-05), [[EIF4G2]] (-0.61, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF215]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +6.7 | 9e-09 | 36/49 (LoVo, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.68×** | +5.2 | 7e-05 | 35/48 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.006 | 31/48 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.20× | +3.3 | 0.12 | 23/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.14 | 23/48 (LoVo, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.340×** | -20.5 | 0e+00 | 48/49 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.336×** | -19.9 | 0e+00 | 44/44 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -14.6 | 1e-45 | 44/48 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.461×** | -13.6 | 4e-40 | 43/45 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.542×** | -11.2 | 5e-27 | 43/47 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.553×** | -10.8 | 2e-25 | 47/48 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -8.3 | 7e-15 | 36/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.744×** | -8.0 | 1e-13 | 31/48 (SNU-423, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.668×** | -7.4 | 1e-11 | 41/48 (NCI-H1573, C32, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -6.7 | 1e-09 | 3/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.706×** | -6.6 | 2e-09 | 38/48 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -5.5 | 2e-06 | 31/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.827×** | -5.1 | 1e-05 | 25/49 (CHP-212, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -5.1 | 2e-05 | 25/48 (SNU-423, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.789×** | -4.5 | 3e-04 | 33/48 (H4, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.791×** | -4.5 | 3e-04 | 30/48 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.794×** | -4.4 | 4e-04 | 29/48 (NCI-H1573, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.795×** | -4.4 | 4e-04 | 27/48 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.825×** | -3.7 | 0.007 | 25/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.4 | 0.017 | 24/48 (COLO 205, HOP62, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.017 | 22/49 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.019 | 21/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.839× | -3.2 | 0.030 | 18/48 (C32, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 793 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -26.1) |
| [[MIA PaCa-2 (line)]] | alt | 370 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -12.9) |
| [[SNU-423 (line)]] | alt | 240 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.4) |
| [[A-172 (line)]] | wt | 203 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 210 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 277 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -26.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 222 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -14.4) |
| [[HS-578T (line)]] | alt | 196 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.461× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 184 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -22.4) |
| [[NCI-H460 (line)]] | wt | 232 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.403× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 251 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.341× (z -11.1) |
| [[SW 900 (line)]] | alt | 218 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -14.1) |
| [[SW480 (line)]] | alt | 223 | 3 (3 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.37× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.260× (z -19.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 224 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.505× (z -8.8) |
| [[J82 (line)]] | alt | 166 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.9) |
| [[PANC-1 (line)]] | alt | 200 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.577× (z -10.0) |
| [[AN3 CA (line)]] | alt | 258 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.6) |
| [[AsPC-1 (line)]] | alt | 154 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -14.7) |
| [[H4 (line)]] | wt | 300 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.255× (z -11.1) |
| [[HOP62 (line)]] | alt | 287 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -16.4) |
| [[Hs 766T (line)]] | wt | 206 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 221 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.414× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.563× (z -10.9) |
| [[A-427 (line)]] | wt | 167 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -28.2) |
| [[C-33 A (line)]] | alt | 265 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.554× (z -8.6) |
| [[CHP-212 (line)]] | wt | 281 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 211 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -14.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 202 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 178 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.653× (z -8.6) |
| [[SW48 (line)]] | wt | 243 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -12.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 356 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -17.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 269 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -25.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -10.4) |
| [[RKO (line)]] | wt | 297 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -13.2) |
| [[SNU-1 (line)]] | wt | 213 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0676× (z -26.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.263× (z -8.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 96.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -8.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.478× (z -9.3) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 367 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35E1]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 |  |
| [[POM121C]] | +0.82 | +0.91 / +0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[POM121]] | +0.80 | +0.87 / +0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RNMT]] | +0.74 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[FUT11]] | +0.71 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[TBC1D20]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMFB]] | -0.64 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[SGPL1]] | -0.62 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CCDC50]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NCOA4]] | -0.59 | -0.57 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF215]] | B | ZNF215 activity raises PRKRIP1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.22× lower at baseline in the lines without ZNF215 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[GPR155]] | B | GPR155 activity raises PRKRIP1's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without GPR155 | 0.094 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity raises PRKRIP1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.53× lower at baseline in the lines without CFL2 | 0.097 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent |
| [[IKBIP]] | C | IKBIP activity raises PRKRIP1's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without IKBIP | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, -20.0); signed map (-41.0, 22.2). **Vector** length 153, 59.6% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.7 | -3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +4.2 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.1 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +5.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.7 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.3 | -8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.7 | -7.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.8 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.5 | -4.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PRKR interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,363,872-102,426,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C114, FLJ13902, KRBOX3 |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H875](https://www.uniprot.org/uniprotkb/Q9H875) (PRKR-interacting protein 1):

> Required for pre-mRNA splicing as component of the spliceosome. Binds double-stranded RNA. Inhibits EIF2AK2 kinase activity (By similarity).

**Summary**, from NCBI Gene [79706](https://www.ncbi.nlm.nih.gov/gene/79706):

> Predicted to enable double-stranded RNA binding activity; protein kinase binding activity; and protein kinase inhibitor activity. Involved in renal system process. Located in actin cytoskeleton and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21894) · Entrez [79706](https://www.ncbi.nlm.nih.gov/gene/79706) · UniProt [Q9H875](https://www.uniprot.org/uniprotkb/Q9H875) · Ensembl [ENSG00000128563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128563)

## Data

Gene col 4891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4891); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4891]; `tensor/DDL_lfc|DDL_z.npy` [4891]; `embed/gene_vectors.npy` [4891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4891 or target_col == 4891). Every well: [[PRKRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
