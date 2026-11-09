---
symbol: "CCNY"
type: "gene"
col: 2918
ensembl_id: "ENSG00000108100"
name: "cyclin Y"
location: "10p11.21"
module: 163
arm: "+"
pooled_cpm: 267.82
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# CCNY

*cyclin Y* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.97× (z +7.7, q 8e-12, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.566× (z -17.4, q 0e+00, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAR1]] (+0.72, fdr 7e-06), [[METAP1]] (+0.71, fdr 1e-05), [[MFSD14B]] (+0.69, fdr 7e-06); moves opposite to [[ZNF764]] (-0.68, fdr 3e-05), [[MYSM1]] (-0.68, fdr 1e-05), [[ZNF24]] (-0.65, fdr 2e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYBU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +7.7 | 8e-12 | 35/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +7.0 | 5e-10 | 28/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +7.0 | 5e-10 | 32/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.9 | 2e-04 | 28/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +4.5 | 9e-04 | 28/49 (SNU-423, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.002 | 25/48 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +4.2 | 0.002 | 24/48 (SK-MEL-2, SNU-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.1 | 0.003 | 11/48 (A498, NCI-H2030, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.1 | 0.003 | 17/49 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.017 | 19/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.039 | 13/47 (SNU-1, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.089 | 22/48 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -17.4 | 0e+00 | 43/49 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -16.2 | 0e+00 | 45/48 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -15.2 | 0e+00 | 40/44 (LS 180, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.524×** | -14.0 | 3e-42 | 43/49 (NCI-H2347, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -10.7 | 9e-25 | 43/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -8.8 | 1e-16 | 43/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.677×** | -8.4 | 3e-15 | 36/48 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -8.4 | 3e-15 | 38/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -8.3 | 8e-15 | 33/48 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.687×** | -7.5 | 3e-12 | 29/45 (A-427, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -7.5 | 4e-12 | 34/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.742×** | -6.2 | 2e-08 | 30/50 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.762×** | -5.9 | 2e-07 | 37/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.791×** | -5.1 | 2e-05 | 29/48 (LS 180, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.791×** | -4.9 | 4e-05 | 28/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -4.5 | 3e-04 | 19/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -4.0 | 0.002 | 23/48 (LS 180, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 304 | 0 | 17 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -23.1) |
| [[HT-29 (line)]] | alt | 381 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -17.5) |
| [[LS 180 (line)]] | wt | 496 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 630 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -22.0) |
| [[KATO III (line)]] | alt | 347 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -18.2) |
| [[BT-474 (line)]] | alt | 309 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -19.9) |
| [[C32 (line)]] | wt | 133 | 3 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.99× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 335 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -15.3) |
| [[HOP62 (line)]] | alt | 237 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -17.7) |
| [[SW480 (line)]] | alt | 234 | 3 (1 ⚠) | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.95× (z +16.2) | [[Auranofin (drug)]] 5 µM 0.449× (z -15.6) |
| [[A-172 (line)]] | wt | 242 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -19.4) |
| [[J82 (line)]] | alt | 205 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 360 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -22.9) |
| [[HS-578T (line)]] | alt | 321 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -18.7) |
| [[LoVo (line)]] | wt | 243 | 2 (2 ⚠) | 5 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.85× (z +10.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -17.6) |
| [[LOX-IMVI (line)]] | wt | 313 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -17.9) |
| [[NCI-H1573 (line)]] | alt | 223 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -18.8) |
| [[RKO (line)]] | wt | 361 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -15.1) |
| [[A498 (line)]] | wt | 199 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.407× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -13.7) |
| [[A-427 (line)]] | wt | 250 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.649× (z -10.0) |
| [[A549 (line)]] | wt | 303 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -18.4) |
| [[NCI-H2030 (line)]] | alt | 293 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.570× (z -10.5) |
| [[PANC-1 (line)]] | alt | 200 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -15.3) |
| [[SNU-423 (line)]] | alt | 211 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -17.2) |
| [[SW1417 (line)]] | alt | 261 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.08× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -9.2) |
| [[SW48 (line)]] | wt | 281 | 3 | 1 | [[TAK-901 (drug)]] 0.05 µM 3.38× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.7) |
| [[C-33 A (line)]] | alt | 399 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 428 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 222 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 172 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.44× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.552× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 253 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 222 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 319 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.20× (z +11.0) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -15.3) |
| [[SNU-1 (line)]] | wt | 261 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -18.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 275 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 307 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 254 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.410× (z -12.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -9.6) |
| [[SHP-77 (line)]] | alt | 276 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[METAP1]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[MFSD14B]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[GPD1L]] | +0.68 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[MBD2]] | +0.67 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.66 | +0.75 / +0.42 | both halves | 4e-05 |  |
| [[SRPK2]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[XPR1]] | +0.63 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[REPS1]] | +0.63 | +0.67 / +0.39 | both halves | 6e-05 |  |
| [[UBE2G1]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[FBXO31]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.62 | +0.68 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | -0.68 | -0.74 / -0.46 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.68 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ZNF24]] | -0.65 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[PLA2G4C]] | -0.64 | -0.71 / -0.39 | both halves | 6e-05 |  |
| [[C11orf58]] | -0.63 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[FAM200A]] | -0.61 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[ZNF776]] | -0.61 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[HELQ]] | -0.61 | -0.71 / -0.47 | both halves | 2e-05 |  |
| [[LARP7]] | -0.61 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[THAP9]] | -0.60 | -0.68 / -0.27 | both halves | 3e-04 |  |
| [[ZBTB1]] | -0.60 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ZNF441]] | -0.60 | -0.63 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYBU]] | B | SYBU activity raises CCNY's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without SYBU | 0.052 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |
| [[TOP2A]] | B | TOP2A activity raises CCNY's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.8, -6.8); signed map (-41.2, -14.4). **Vector** length 106, 37.2% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.3 | +7.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.3 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.3 | -16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.0 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | +0.2 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin Y |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.21 — chr10:35,247,025-35,572,669 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CFP1, CBCP1; previously C10orf9 |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND76](https://www.uniprot.org/uniprotkb/Q8ND76) (Cyclin-Y):

> Positive regulatory subunit of the cyclin-dependent kinases CDK14/PFTK1 and CDK16. Acts as a cell-cycle regulator of Wnt signaling pathway during G2/M phase by recruiting CDK14/PFTK1 to the plasma membrane and promoting phosphorylation of LRP6, leading to the activation of the Wnt signaling pathway. Recruits CDK16 to the plasma membrane. Isoform 3 might play a role in the activation of MYC-mediated transcription.

**Summary**, from NCBI Gene [219771](https://www.ncbi.nlm.nih.gov/gene/219771):

> Cyclins, such as CCNY, control cell division cycles and regulate cyclin-dependent kinases (e.g., CDC2; MIM 116940) (Li et al., 2009 [PubMed 18060517]).[supplied by OMIM, May 2009]

**Accessions** — [HGNC:23354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23354) · Entrez [219771](https://www.ncbi.nlm.nih.gov/gene/219771) · UniProt [Q8ND76](https://www.uniprot.org/uniprotkb/Q8ND76) · Ensembl [ENSG00000108100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108100)

## Data

Gene col 2918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2918); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2918]; `tensor/DDL_lfc|DDL_z.npy` [2918]; `embed/gene_vectors.npy` [2918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2918 or target_col == 2918). Every well: [[CCNY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
