---
symbol: "FTH1"
type: "gene"
col: 9575
ensembl_id: "ENSG00000167996"
name: "ferritin heavy chain 1"
location: "11q12.3"
module: 139
arm: "+"
pooled_cpm: 524.07
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 15
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# FTH1

*ferritin heavy chain 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +11.6, q 4e-28, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.45× (z +9.3, q 3e-18, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.495× (z -10.2, q 9e-22, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEST1]] (+0.75, fdr 7e-06, ⚠ same locus), [[CPD]] (+0.61, fdr 1e-05), [[SOD2]] (+0.60, fdr 1e-05), [[NFIL3]] (+0.59, fdr 7e-06); moves opposite to [[SIPA1L3]] (-0.50, fdr 5e-05), [[LINC00973]] (-0.49, fdr 4e-05), [[GALNT6]] (-0.46, fdr 4e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SAA2-SAA4]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +11.6 | 4e-28 | 44/45 (HEC-1-A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +9.3 | 3e-18 | 38/44 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +8.4 | 1e-14 | 39/41 (HEC-1-A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.7 | 1e-12 | 36/41 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.009 | 39/44 (A498, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.015 | 34/44 (HCT15, HT-29, …) | all doses, stronger at high dose |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.069 | 37/44 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.2 | 0.090 | 21/44 (A-427, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Erlotinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.090 | 34/43 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.14 | 23/44 (H4, HOP62, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.50× | +3.0 | 0.14 | 31/44 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.495×** | -10.2 | 9e-22 | 36/44 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.780×** | -8.6 | 2e-15 | 41/46 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -6.3 | 5e-08 | 37/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.682×** | -5.5 | 4e-06 | 44/44 (SHP-77, BT-474, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.618×** | -4.7 | 2e-04 | 42/44 (CFPAC-1, A-427, …) | top dose only | position effect removed |
| [[Delamanid (drug)]] 0.05 µM |  | **0.659×** | -4.3 | 0.002 | 42/44 (SW480, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **0.760×** | -3.9 | 0.006 | 41/44 (SW1417, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.672×** | -3.9 | 0.006 | 41/44 (LoVo, PANC-1, …) | rises with dose | position effect removed |
| [[Finasteride (drug)]] 5 µM |  | **0.675×** | -3.9 | 0.007 | 42/44 (LoVo, LS 180, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -3.6 | 0.016 | 24/44 (A498, A549, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.695×** | -3.6 | 0.017 | 40/43 (HCT15, SW480, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.614×** | -3.6 | 0.017 | 40/44 (NCI-H23, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -3.5 | 0.023 | 25/44 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.701×** | -3.4 | 0.024 | 32/43 (BT-474, A-172, …) | inconsistent across doses | position effect removed |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **0.739×** | -3.1 | 0.077 | 32/44 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 225 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 704 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.17× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 179 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.46× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 403 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.16× (z +9.7) | — |
| [[LoVo (line)]] | wt | 244 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.69× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 925 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.2) |
| [[SW480 (line)]] | alt | 235 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.19× (z +12.8) | — |
| [[A-427 (line)]] | wt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +14.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 487 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 6.38× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.3) |
| [[HCT15 (line)]] | alt | 311 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 0.5 µM 3.57× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 937 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.01× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.0) |
| [[KATO III (line)]] | alt | 587 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 3.17× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 165 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.28× (z +10.8) | — |
| [[A549 (line)]] | wt | 932 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 855 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.9) |
| [[H4 (line)]] | wt | 365 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 522 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 1,164 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 181 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 545 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.98× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 477 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 459 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.29× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.2) |
| [[A498 (line)]] | wt | 691 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -9.1) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 301 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 956 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 919 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.6) |
| [[CHP-212 (line)]] | wt | 207 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 276 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 318 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 450 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 564 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 299 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 419 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.2) |
| [[SNU-423 (line)]] | alt | 979 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.0) |
| [[SW 1271 (line)]] | alt | 443 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.5) |
| [[SW 900 (line)]] | alt | 974 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -15.1) |
| [[SW48 (line)]] | wt | 253 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.25× (z +9.4) | — |
| [[A-172 (line)]] | wt | 341 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 656 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 421 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1,091 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 570 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 455 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 129 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 79.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1,056 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 894 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEST1]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CPD]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis; STRING 517 |
| [[SOD2]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 | STRING 501 |
| [[NFIL3]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PSAP]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NAMPTP1]] | +0.54 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[B4GALT1]] | +0.53 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NCOA3]] | +0.53 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[C1RL]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CTSD]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SNX3]] | +0.52 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIPA1L3]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[LINC00973]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GALNT6]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[EVA1A]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PDSS1]] | -0.45 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[MARCHF4]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PRR7-AS1]] | -0.44 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MANCR]] | -0.44 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[CEP135]] | -0.43 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[SIGLEC15]] | -0.43 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[PHLDB1]] | -0.43 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[SMG9]] | -0.43 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAA2-SAA4]] | B | SAA2-SAA4 activity raises FTH1's level | lines that do not express SAA2-SAA4 (22) vs lines expressing it (28) | 2.31× lower at baseline in the lines without SAA2-SAA4 | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[CP]] | B | CP activity raises FTH1's level | lines that do not express CP (39) vs lines expressing it (11) | 2.04× lower at baseline in the lines without CP | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[SAA2]] | B | SAA2 activity raises FTH1's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without SAA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | C | FTH1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.28× the cells of the other lines | 0.007 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Hydroxyfasudil (drug)]] 5 µM | C | FTH1 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 1.34× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| [[EPAS1]] | C | FTH1 activity raises EPAS1's level | lines that do not express FTH1 (4) vs lines expressing it (46) | 5.02× lower at baseline in the lines without FTH1 | 0.024 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | C | FTH1 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.74× the cells of the other lines | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Radotinib (drug)]] 5 µM | C | FTH1 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.83× the cells of the other lines | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.5 µM | C | FTH1 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.19× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | FTH1 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.43× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | FTH1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.61× the cells of the other lines | 0.056 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 5 µM | C | FTH1 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.20× the cells of the other lines | 0.065 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.05 µM | C | FTH1 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.31× the cells of the other lines | 0.074 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | FTH1 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.78× the cells of the other lines | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| [[ITM2B]] | C | FTH1 activity raises ITM2B's level | lines that do not express FTH1 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without FTH1 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 17.2); signed map (17.8, 27.2). **Vector** length 140, 45.7% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.3 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.1 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.0 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -10.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.1 | -1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -4.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ferritin heavy chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:61,959,718-61,967,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FTH, PLIF, PIG15, FHC; previously FTHL6 |
| Gene groups (HGNC) | Ferritin chains; Ferritin ferroxidases |
| Reactome | 10 pathways, smallest: Scavenging by Class A Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P02794](https://www.uniprot.org/uniprotkb/P02794) (Ferritin heavy chain):

> Stores iron in a soluble, non-toxic, readily available form. Important for iron homeostasis. Has ferroxidase activity. Iron is taken up in the ferrous form and deposited as ferric hydroxides after oxidation. Also plays a role in delivery of iron to cells (By similarity). Mediates iron uptake in capsule cells of the developing kidney (By similarity). Delivery to lysosomes is mediated by the cargo receptor NCOA4 for autophagic degradation and release of iron.

**Summary**, from NCBI Gene [2495](https://www.ncbi.nlm.nih.gov/gene/2495):

> This gene encodes the heavy subunit of ferritin, the major intracellular iron storage protein in prokaryotes and eukaryotes. It is composed of 24 subunits of the heavy and light ferritin chains. Variation in ferritin subunit composition may affect the rates of iron uptake and release in different tissues. A major function of ferritin is the storage of iron in a soluble and nontoxic state. Defects in ferritin proteins are associated with several neurodegenerative diseases. This gene has multiple …

**Accessions** — [HGNC:3976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3976) · Entrez [2495](https://www.ncbi.nlm.nih.gov/gene/2495) · UniProt [P02794](https://www.uniprot.org/uniprotkb/P02794) · Ensembl [ENSG00000167996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167996)

## Data

Gene col 9575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9575); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9575]; `tensor/DDL_lfc|DDL_z.npy` [9575]; `embed/gene_vectors.npy` [9575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9575 or target_col == 9575). Every well: [[FTH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
