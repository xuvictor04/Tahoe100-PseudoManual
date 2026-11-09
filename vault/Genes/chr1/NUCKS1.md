---
symbol: "NUCKS1"
type: "gene"
col: 913
ensembl_id: "ENSG00000069275"
name: "nuclear casein kinase and cyclin dependent kinase substrate 1"
location: "1q32.1"
module: 22
arm: "+"
pooled_cpm: 395.75
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NUCKS1

*nuclear casein kinase and cyclin dependent kinase substrate 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.33× (z +15.7, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +3.9, q 0.009, up in 35 of 50 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.508× (z -7.5, q 2e-11, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUSAP1]] (+0.69, fdr 7e-06), [[HMGN2]] (+0.69, fdr 1e-05), [[DLEU2]] (+0.68, fdr 7e-06); moves opposite to [[ST6GALNAC6]] (-0.61, fdr 2e-05), [[NEIL2]] (-0.58, fdr 3e-05), [[ST6GALNAC4]] (-0.58, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.33×** | +15.7 | 0e+00 | 44/44 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.05×** | +14.4 | 3e-44 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +11.6 | 1e-28 | 45/45 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.59×** | +5.1 | 4e-05 | 42/48 (KATO III, SW 900, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **1.55×** | +4.9 | 1e-04 | 44/48 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.56×** | +4.7 | 2e-04 | 37/47 (A-172, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.009 | 35/50 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +3.8 | 0.011 | 35/48 (KATO III, SW 900, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.013 | 25/49 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.042 | 43/48 (SNU-1, A549, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.75×** | +3.3 | 0.054 | 40/47 (HS-578T, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.078 | 39/48 (SNU-423, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.1 | 0.082 | 29/48 (A549, NCI-H1792, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -7.5 | 2e-11 | 48/48 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -7.5 | 2e-11 | 48/48 (HCT15, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.518×** | -7.3 | 6e-11 | 48/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -5.0 | 1e-04 | 43/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.772×** | -4.0 | 0.006 | 34/48 (H4, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.704×** | -3.9 | 0.010 | 41/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.541×** | -3.6 | 0.030 | 43/49 (SNU-1, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.577× | -3.2 | 0.10 | 30/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | 0.738× | -3.0 | 0.17 | 28/48 (SW48, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 598 | 5 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.51× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.547× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 326 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +15.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.352× (z -10.1) |
| [[HCT15 (line)]] | alt | 434 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.264× (z -10.9) |
| [[J82 (line)]] | alt | 528 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +13.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.7) |
| [[A549 (line)]] | wt | 353 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +15.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 401 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +13.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.429× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 353 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +14.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 524 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.08× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.278× (z -10.5) |
| [[KATO III (line)]] | alt | 265 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 601 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 570 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.340× (z -10.3) |
| [[SW 900 (line)]] | alt | 475 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 509 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +14.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 161 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 501 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +14.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 227 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 533 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +16.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 348 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.94× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 265 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 277 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +14.3) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 341 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +14.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 358 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +13.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 514 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.25× (z +14.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 222 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 206 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.77× (z +16.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 301 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 375 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +15.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 491 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +14.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 251 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +12.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 301 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 354 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.329× (z -9.4) |
| [[SNU-423 (line)]] | alt | 340 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 281 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 444 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 397 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +12.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 371 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 831 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 243 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 231 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 322 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 306 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 409 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 314 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 623 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +8.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 220 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.72× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 722 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 407 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUSAP1]] | +0.69 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[HMGN2]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[DLEU2]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SNHG31]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[HMGB2]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[PCM1]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PRC1]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[TPX2]] | +0.63 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[SKA2]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[HMMR]] | +0.63 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[HMGB1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RMI1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[NEIL2]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.58 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[CTU1]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[WDR55]] | -0.57 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[LRFN3]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[HMOX2]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[FCHSD1]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[GTF2E2]] | -0.56 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[RBAK-RBAKDN]] | -0.55 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[LINC02693]] | -0.55 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CSK]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NUCKS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HYLS1]] | B | HYLS1 activity raises NUCKS1's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without HYLS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[SPDL1]] | C | SPDL1 activity raises NUCKS1's level | lines that do not express SPDL1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.0, -53.0); signed map (-49.5, -48.1). **Vector** length 102, 52.1% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.50 to 28); *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.55 to 8); *Kinesins* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | -1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | -0.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | -4.9 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear casein kinase and cyclin dependent kinase substrate 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,712,822-205,750,182 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NUCKS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1E3](https://www.uniprot.org/uniprotkb/Q9H1E3) (Nuclear ubiquitous casein and cyclin-dependent kinase substrate 1):

> Chromatin-associated protein involved in DNA repair by promoting homologous recombination (HR). Binds double-stranded DNA (dsDNA) and secondary DNA structures, such as D-loop structures, but with less affinity than RAD51AP1.

**Summary**, from NCBI Gene [64710](https://www.ncbi.nlm.nih.gov/gene/64710):

> This gene encodes a nuclear protein that is highly conserved in vertebrates. The conserved regions of the protein contain several consensus phosphorylation sites for casein kinase II and cyclin-dependent kinases, two putative nuclear localization signals, and a basic DNA-binding domain. It is phosphorylated in vivo by Cdk1 during mitosis of the cell cycle. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:29923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29923) · Entrez [64710](https://www.ncbi.nlm.nih.gov/gene/64710) · UniProt [Q9H1E3](https://www.uniprot.org/uniprotkb/Q9H1E3) · Ensembl [ENSG00000069275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069275)

## Data

Gene col 913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 913); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 913]; `tensor/DDL_lfc|DDL_z.npy` [913]; `embed/gene_vectors.npy` [913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 913 or target_col == 913). Every well: [[NUCKS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUCKS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
