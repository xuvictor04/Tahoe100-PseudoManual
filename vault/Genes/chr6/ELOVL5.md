---
symbol: "ELOVL5"
type: "gene"
col: 258
ensembl_id: "ENSG00000012660"
name: "ELOVL fatty acid elongase 5"
location: "6p12.1"
module: 170
arm: "-"
pooled_cpm: 117.99
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 10
n_dd_up_clean: 21
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# ELOVL5

*ELOVL fatty acid elongase 5* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.25× (z +15.9, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.763× (z -5.2, q 9e-05, down in 29 of 42 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.710× (z -4.7, q 8e-04, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHCR24]] (+0.61, fdr 1e-05), [[MSMO1]] (+0.60, fdr 1e-05), [[DHCR7]] (+0.60, fdr 7e-06); moves opposite to [[UTP23]] (-0.61, fdr 1e-05), [[ALKBH1]] (-0.61, fdr 7e-06), [[TJAP1]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[RNF169]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.25×** | +15.9 | 0e+00 | 41/42 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +13.8 | 1e-40 | 41/42 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.76×** | +13.2 | 1e-37 | 40/41 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +12.6 | 3e-34 | 33/42 (C32, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +12.1 | 2e-31 | 40/42 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.44×** | +12.0 | 2e-31 | 42/42 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +12.0 | 3e-31 | 41/42 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.22×** | +10.8 | 2e-25 | 39/42 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.17×** | +9.9 | 2e-21 | 41/42 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +9.0 | 9e-18 | 37/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.18×** | +8.2 | 1e-14 | 37/39 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +7.3 | 1e-11 | 34/42 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +7.2 | 3e-11 | 36/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.09×** | +6.6 | 2e-09 | 38/43 (CFPAC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +6.5 | 4e-09 | 28/43 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.38×** | +6.1 | 5e-08 | 33/42 (SNU-423, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +5.9 | 1e-07 | 32/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 3e-07 | 31/42 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.763×** | -5.2 | 9e-05 | 29/42 (AsPC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.710×** | -4.7 | 8e-04 | 27/42 (A498, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.717×** | -4.6 | 1e-03 | 34/42 (LoVo, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.746×** | -4.0 | 0.008 | 23/42 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.029 | 23/41 (MIA PaCa-2, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.674×** | -3.6 | 0.035 | 26/42 (SNU-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.071 | 20/42 (Hs 766T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.071 | 20/42 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.789×** | -3.3 | 0.071 | 23/42 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **0.791×** | -3.2 | 0.071 | 17/42 (SW 1088, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.801× | -3.1 | 0.12 | 17/42 (SNU-1, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.2 | 14 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.92× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 90.3 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 50.2 | 13 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +13.3) | — |
| [[LoVo (line)]] | wt | 66.0 | 12 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.57× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 128 | 11 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.54× (z +15.2) | — |
| [[A-172 (line)]] | wt | 56.4 | 10 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.99× (z +15.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 5.61× (z +14.2) | — |
| [[C32 (line)]] | wt | 75.7 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +18.0) | — |
| [[SW480 (line)]] | alt | 110 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 60.1 | 9 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.80× (z +16.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 5.90× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 87.4 | 7 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.14× (z +13.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 4.48× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 297 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.98× (z +14.4) | — |
| [[SW1417 (line)]] | alt | 86.6 | 7 | 0 | [[Auranofin (drug)]] 5 µM 5.66× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 112 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 194 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 183 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 109 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.9) | — |
| [[J82 (line)]] | alt | 152 | 5 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.46× (z +11.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 3.08× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 121 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 112 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.93× (z +13.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.8) | — |
| [[A498 (line)]] | wt | 285 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.44× (z +12.4) | — |
| [[A549 (line)]] | wt | 72.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.00× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 106 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 37.1 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 22.1× (z +15.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[H4 (line)]] | wt | 131 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 106 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 124 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.35× (z +12.6) | — |
| [[A-427 (line)]] | wt | 137 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.74× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.5) |
| [[AN3 CA (line)]] | alt | 401 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 128 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 130 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 145 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 152 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.29× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 58.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 234 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.22× (z +14.7) ⚠ toxic | — |
| [[BT-474 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHCR24]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[MSMO1]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 | STRING 418 |
| [[DHCR7]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 452 |
| [[TMEM97]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PSME4]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[STARD4]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[FADS1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 836 |
| [[LRP8]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FDFT1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[HMGCR]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 441 |
| [[HMGCS1]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 429 |
| [[FASN]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 695 |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP23]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ALKBH1]] | -0.61 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[TJAP1]] | -0.60 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[COIL]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ABRAXAS2]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ZNF264]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[YJU2B]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RNF111]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ZNF136]] | -0.56 | -0.46 / -0.55 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression |
| [[LATS1]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ANKRD49]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CCDC174]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF169]] | B | ELOVL5 activity lowers RNF169's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 1.25× higher at baseline in the lines without ELOVL5 | 0.058 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |
| [[MSMO1]] | B | ELOVL5 activity lowers MSMO1's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 1.91× higher at baseline in the lines without ELOVL5 | 0.072 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |
| [[FADS1]] | B | ELOVL5 activity raises FADS1's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 5.59× lower at baseline in the lines without ELOVL5 | 0.074 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |
| [[TECR]] | B | ELOVL5 activity raises TECR's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 1.17× lower at baseline in the lines without ELOVL5 | 0.076 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (21.6, -50.7); signed map (-50.8, 31.7). **Vector** length 115, 41.0% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +15.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.7 | +13.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.5 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +10.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.0 | +5.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.7 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ELOVL fatty acid elongase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:53,267,398-53,349,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HELO1, dJ483K16.1; previously SCA38 |
| Gene groups (HGNC) | ELOVL fatty acid elongase family |
| Hallmark sets | PEROXISOME, ANDROGEN_RESPONSE, FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: Linoleic acid (LA) metabolism; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism; alpha-linolenic acid (ALA) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYP7](https://www.uniprot.org/uniprotkb/Q9NYP7) (Very long chain fatty acid elongase 5):

> Catalyzes the first and rate-limiting reaction of the four reactions that constitute the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle. Condensing enzyme that acts specifically toward polyunsaturated acyl-CoA with the higher activity toward C18:3(n-6) acyl-CoA. May participate in the production of monounsaturated and of polyunsaturated VLCFAs of …

**Summary**, from NCBI Gene [60481](https://www.ncbi.nlm.nih.gov/gene/60481):

> This gene belongs to the ELO family. It is highly expressed in the adrenal gland and testis, and encodes a multi-pass membrane protein that is localized in the endoplasmic reticulum. This protein is involved in the elongation of long-chain polyunsaturated fatty acids. Mutations in this gene have been associated with spinocerebellar ataxia-38 (SCA38). Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:21308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21308) · Entrez [60481](https://www.ncbi.nlm.nih.gov/gene/60481) · UniProt [Q9NYP7](https://www.uniprot.org/uniprotkb/Q9NYP7) · Ensembl [ENSG00000012660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012660)

## Data

Gene col 258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 258); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 258]; `tensor/DDL_lfc|DDL_z.npy` [258]; `embed/gene_vectors.npy` [258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 258 or target_col == 258). Every well: [[ELOVL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOVL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
