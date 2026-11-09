---
symbol: "GPI"
type: "gene"
col: 2563
ensembl_id: "ENSG00000105220"
name: "glucose-6-phosphate isomerase"
location: "19q13.11"
module: 99
arm: "+"
pooled_cpm: 377.62
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 45
n_dd_up_clean: 4
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# GPI

*glucose-6-phosphate isomerase* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.34× (z +4.2, q 0.013, up in 32 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Pravastatin (sodium) (drug)]] 5 µM: 1.34× (z +3.7, q 0.036, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.166× (z -36.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFKFB4]] (+0.76, fdr 7e-06), [[PDK3]] (+0.74, fdr 7e-06), [[ERO1A]] (+0.71, fdr 7e-06); moves opposite to [[GABPB1]] (-0.60, fdr 3e-05), [[HSPBAP1]] (-0.58, fdr 1e-05), [[ZC3H12C]] (-0.57, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.2 | 0.013 | 32/47 (HT-29, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.0 | 0.015 | 35/47 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.7 | 0.036 | 25/48 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.036 | 37/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.051 | 34/48 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[venetoclax (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.070 | 29/47 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.070 | 27/47 (HT-29, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.16× | +3.1 | 0.14 | 16/47 (CFPAC-1, CHP-212, …) | top dose only | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 1.28× | +3.0 | 0.16 | 20/47 (COLO 205, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.166×** | -36.9 | 0e+00 | 47/47 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.207×** | -22.9 | 0e+00 | 47/47 (AN3 CA, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.282×** | -15.6 | 0e+00 | 47/47 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.491×** | -8.8 | 2e-16 | 44/47 (C-33 A, COLO 205, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.655×** | -8.7 | 4e-16 | 45/47 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -8.4 | 3e-15 | 36/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.629×** | -6.7 | 1e-09 | 36/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -6.5 | 7e-09 | 33/47 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -6.3 | 1e-08 | 34/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -6.2 | 3e-08 | 35/47 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -6.2 | 3e-08 | 40/47 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -6.0 | 8e-08 | 36/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -5.6 | 8e-07 | 36/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.690×** | -5.4 | 3e-06 | 36/47 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.706×** | -5.1 | 2e-05 | 40/47 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -4.3 | 6e-04 | 26/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.751×** | -4.2 | 9e-04 | 31/47 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.577×** | -4.2 | 9e-04 | 39/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.735×** | -4.1 | 0.001 | 29/47 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.002 | 31/47 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 737 | 0 | 28 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -32.8) |
| [[C-33 A (line)]] | alt | 683 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -24.9) |
| [[COLO 205 (line)]] | alt | 520 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -30.4) |
| [[BT-474 (line)]] | alt | 385 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -25.0) |
| [[SW480 (line)]] | alt | 418 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -34.0) |
| [[NCI-H460 (line)]] | wt | 391 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -31.2) |
| [[A-172 (line)]] | wt | 364 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -21.2) |
| [[MIA PaCa-2 (line)]] | alt | 606 | 1 (1 ⚠) | 5 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +14.9) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -28.3) |
| [[A498 (line)]] | wt | 167 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +16.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -10.4) |
| [[A549 (line)]] | wt | 612 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -25.0) |
| [[C32 (line)]] | wt | 426 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -22.0) |
| [[HEC-1-A (line)]] | alt | 571 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -31.5) |
| [[HT-29 (line)]] | alt | 473 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -31.8) |
| [[LOX-IMVI (line)]] | wt | 345 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -26.9) |
| [[Panc 03.27 (line)]] | alt | 456 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -35.3) |
| [[RPMI-7951 (line)]] | alt | 602 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -27.5) |
| [[H4 (line)]] | wt | 845 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -28.4) |
| [[HCT15 (line)]] | alt | 358 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -24.4) |
| [[Hs 766T (line)]] | wt | 399 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -34.2) |
| [[KATO III (line)]] | alt | 380 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -29.6) |
| [[NCI-H1792 (line)]] | alt | 358 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.7) |
| [[SNU-423 (line)]] | alt | 212 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -26.2) |
| [[A-427 (line)]] | wt | 200 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -29.0) |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -26.1) |
| [[CFPAC-1 (line)]] | alt | 395 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -26.4) |
| [[CHP-212 (line)]] | wt | 472 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0706× (z -28.9) |
| [[HS-578T (line)]] | alt | 202 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -25.3) |
| [[J82 (line)]] | alt | 386 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -28.6) |
| [[LoVo (line)]] | wt | 333 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -30.3) |
| [[LS 180 (line)]] | wt | 355 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -31.0) |
| [[NCI-H2030 (line)]] | alt | 216 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -27.7) |
| [[NCI-H2347 (line)]] | alt | 293 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -26.6) |
| [[PANC-1 (line)]] | alt | 344 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -28.5) |
| [[RKO (line)]] | wt | 248 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -25.0) |
| [[SHP-77 (line)]] | alt | 353 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -22.0) |
| [[SNU-1 (line)]] | wt | 639 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -21.9) |
| [[SW 900 (line)]] | alt | 360 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.0) |
| [[SW1417 (line)]] | alt | 179 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -24.3) |
| [[SW48 (line)]] | wt | 399 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.1) |
| [[AN3 CA (line)]] | alt | 323 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0325× (z -28.7) |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -24.2) |
| [[HOP62 (line)]] | alt | 633 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -26.0) |
| [[NCI-H23 (line)]] | alt | 191 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -23.5) |
| [[NCI-H661 (line)]] | alt | 374 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.7) |
| [[hTERT-HPNE (line)]] | wt | 99.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.6) |
| [[SW 1271 (line)]] | alt | 318 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -16.1) |
| [[NCI-H2122 (line)]] | alt | 419 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 429 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFKFB4]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Glucose metabolism; STRING 745 |
| [[PDK3]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 505 |
| [[ERO1A]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[NXPH4]] | +0.68 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CDON]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[PGK1]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 971 |
| [[INSIG2]] | +0.67 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.64 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.63 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[LRP1]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1]] | -0.60 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[HSPBAP1]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZC3H12C]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ITPA]] | -0.56 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[MOSMO]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GNG12-AS1]] | -0.54 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[CFLAR]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.53 | -0.64 / -0.32 | both halves | 2e-04 |  |
| [[AVEN]] | -0.52 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[SLC35G2]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[NIPAL2]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MSRA]] | -0.52 | -0.58 / -0.38 | both halves | 6e-05 | STRING 441 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GPI's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDON]] | C | CDON activity raises GPI's level | lines that do not express CDON (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without CDON | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, -16.0); signed map (-35.8, 24.2). **Vector** length 143, 54.9% of its response variance represented; |z| ≥ 3 in 1,685 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.55 to 7); *glycolysis* (hallmark, mean cos +0.55 to 12); *Regulation of pyruvate metabolism* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +6.6 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +6.1 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.8 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.6 | -6.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.8 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.4 | -8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.6 | -8.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -6.2 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.1 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.9 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.7 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | glucose-6-phosphate isomerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,359,480-34,402,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AMF, NLK |
| Hallmark sets | HYPOXIA, MTORC1_SIGNALING, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P06744](https://www.uniprot.org/uniprotkb/P06744) (Glucose-6-phosphate isomerase):

> Isomerase that catalyzes the conversion of alpha-D-glucose-6-phosphate to beta-D-fructose-6-phosphate, the second step in glycolysis, and the reverse reaction in gluconeogenesis, within the cytoplasm. Also shows C2-epimerase activity, interconverting D-glucose-6-phosphate (G6P) and D-mannose-6-phosphate (M6P) (By similarity). Also displays anomerase activity, interconverting alpha and beta-anomeric forms of G6P, D-fructose-6-phosphate and M6P (By similarity). In addition to its metabolic role, …

**Summary**, from NCBI Gene [2821](https://www.ncbi.nlm.nih.gov/gene/2821):

> This gene encodes a member of the glucose phosphate isomerase protein family. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. In the cytoplasm, the gene product functions as a glycolytic enzyme (glucose-6-phosphate isomerase) that interconverts glucose-6-phosphate and fructose-6-phosphate. Extracellularly, the encoded protein (also referred to as neuroleukin) functions as a neurotrophic factor that promotes …

**Accessions** — [HGNC:4458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4458) · Entrez [2821](https://www.ncbi.nlm.nih.gov/gene/2821) · UniProt [P06744](https://www.uniprot.org/uniprotkb/P06744) · Ensembl [ENSG00000105220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105220)

## Data

Gene col 2563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2563); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2563]; `tensor/DDL_lfc|DDL_z.npy` [2563]; `embed/gene_vectors.npy` [2563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2563 or target_col == 2563). Every well: [[GPI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
