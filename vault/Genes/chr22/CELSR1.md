---
symbol: "CELSR1"
type: "gene"
col: 1110
ensembl_id: "ENSG00000075275"
name: "cadherin EGF LAG seven-pass G-type receptor 1"
location: "22q13.31"
module: 34
arm: "+"
pooled_cpm: 84.87
n_lines_expressing: 43
n_dd_up: 2
n_dd_down: 38
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 12
direction_downstream: 10
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CELSR1

*cadherin EGF LAG seven-pass G-type receptor 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.25× (z +4.3, q 0.009, up in 21 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -24.9, q 0e+00, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM255B]] (+0.66, fdr 7e-06), [[GALNT12]] (+0.63, fdr 1e-05), [[WNT7B]] (+0.61, fdr 7e-06); moves opposite to [[SORBS2]] (-0.57, fdr 1e-05), [[CAVIN2]] (-0.53, fdr 1e-05), [[DECR1]] (-0.52, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SYT17]] → it (grade B ⚠); 10 go from it, the strongest it → [[RHBDF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.009 | 21/40 (H4, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.25×** | +4.2 | 0.009 | 18/40 (H4, C32, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.15× | +3.8 | 0.024 | 15/41 (LoVo, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.400×** | -24.9 | 0e+00 | 36/41 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -16.7 | 0e+00 | 34/42 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.438×** | -15.9 | 0e+00 | 35/41 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.445×** | -15.5 | 0e+00 | 36/41 (HOP62, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.436×** | -15.4 | 0e+00 | 38/41 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.464×** | -14.8 | 0e+00 | 35/41 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.470×** | -14.5 | 1e-45 | 34/41 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -13.3 | 1e-38 | 35/41 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.534×** | -11.6 | 3e-29 | 32/39 (NCI-H1573, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.548×** | -11.6 | 3e-29 | 32/41 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.548×** | -11.5 | 5e-29 | 34/41 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.551×** | -11.4 | 1e-28 | 33/41 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.563×** | -10.6 | 1e-24 | 31/43 (A-172, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.613×** | -8.7 | 1e-16 | 29/36 (A-172, C32, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.734×** | -8.4 | 2e-15 | 24/41 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -7.7 | 3e-13 | 30/42 (HOP62, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.687×** | -7.2 | 2e-11 | 26/41 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -5.4 | 2e-06 | 22/41 (A-172, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -5.2 | 4e-06 | 25/41 (LoVo, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.780×** | -4.8 | 4e-05 | 22/41 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -4.6 | 7e-05 | 20/41 (A-172, Hs 766T, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.794×** | -4.2 | 4e-04 | 20/42 (A549, Hs 766T, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.660×** | -4.2 | 6e-04 | 21/40 (C32, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 207 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -27.0) |
| [[PANC-1 (line)]] | alt | 88.9 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -23.4) |
| [[C32 (line)]] | wt | 200 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -29.9) |
| [[Hs 766T (line)]] | wt | 266 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -23.5) |
| [[A-172 (line)]] | wt | 202 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.4) |
| [[LoVo (line)]] | wt | 73.0 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.5) |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 156 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -21.0) |
| [[HOP62 (line)]] | alt | 128 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 99.6 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -21.1) |
| [[NCI-H1792 (line)]] | alt | 60.3 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -27.4) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -14.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -10.5) |
| [[J82 (line)]] | alt | 48.5 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 55.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -23.5) |
| [[NCI-H2030 (line)]] | alt | 61.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -17.2) |
| [[A549 (line)]] | wt | 146 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -14.5) |
| [[BT-474 (line)]] | alt | 99.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.326× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 81.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.8) |
| [[C-33 A (line)]] | alt | 83.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.5) |
| [[KATO III (line)]] | alt | 44.3 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -11.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.6) |
| [[A-427 (line)]] | wt | 52.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 57.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.8) |
| [[SW 900 (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.0) |
| [[HCT15 (line)]] | alt | 94.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -15.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.5) |
| [[SW480 (line)]] | alt | 38.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.2) |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -11.5) |
| [[H4 (line)]] | wt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.3) |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.4) |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.1) |
| [[SW48 (line)]] | wt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -8.7) |
| [[A498 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM255B]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GALNT12]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[KHDRBS3]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[WSCD1]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TNFRSF11A]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LIMK1]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[STX1A]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[FAM107B]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LTBP4]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TNNT1]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORBS2]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CAVIN2]] | -0.53 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[DECR1]] | -0.52 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[FIGN]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HOPX]] | -0.48 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[FNDC3A]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LUC7L2]] | -0.47 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[ARHGAP24]] | -0.47 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[TTC32]] | -0.47 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[BATF]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[LINC01836]] | -0.46 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[RPRD1B]] | -0.46 | -0.25 / -0.37 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT17]] | B | SYT17 activity raises CELSR1's level | lines that do not express SYT17 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without SYT17 | 0.002 | ⚠ within organs, on part of the lines; also absent: SEPTIN3, STOX2, ULK2; maybe low, not absent |
| [[PDGFB]] | B | PDGFB activity raises CELSR1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without PDGFB | 0.004 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[ARHGEF4]] | B | ARHGEF4 activity raises CELSR1's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without ARHGEF4 | 0.012 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[RHBDF2]] | B | RHBDF2 activity raises CELSR1's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without RHBDF2 | 0.018 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[GALNT12]] | B | GALNT12 activity raises CELSR1's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.42× lower at baseline in the lines without GALNT12 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[CDCP1]] | B | CDCP1 activity raises CELSR1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without CDCP1 | 0.041 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[STOX2]] | B | STOX2 activity raises CELSR1's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without STOX2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[ABTB3]] | B | ABTB3 activity raises CELSR1's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without ABTB3 | 0.062 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[F11R]] | B | F11R activity raises CELSR1's level | lines that do not express F11R (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without F11R | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[MAP3K9]] | B | MAP3K9 activity raises CELSR1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without MAP3K9 | 0.075 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity raises CELSR1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without WNT7B | 0.079 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[ST6GALNAC2]] | C | ST6GALNAC2 activity raises CELSR1's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 3.17× lower at baseline in the lines without ST6GALNAC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHBDF2]] | B | CELSR1 activity raises RHBDF2's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.12× lower at baseline in the lines without CELSR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[CDCP1]] | B | CELSR1 activity raises CDCP1's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.75× lower at baseline in the lines without CELSR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[ARHGEF4]] | B | CELSR1 activity raises ARHGEF4's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 3.17× lower at baseline in the lines without CELSR1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[KRT15]] | B | CELSR1 activity raises KRT15's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.12× lower at baseline in the lines without CELSR1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[MEGF6]] | B | CELSR1 activity raises MEGF6's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.76× lower at baseline in the lines without CELSR1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[SLCO4A1]] | B | CELSR1 activity raises SLCO4A1's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.33× lower at baseline in the lines without CELSR1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[SYT17]] | B | CELSR1 activity raises SYT17's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without CELSR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[STOX2]] | B | CELSR1 activity raises STOX2's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 4.81× lower at baseline in the lines without CELSR1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[WNT9A]] | C | CELSR1 activity raises WNT9A's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 4.56× lower at baseline in the lines without CELSR1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A; co-absent with the target |
| [[ST6GALNAC2]] | C | CELSR1 activity raises ST6GALNAC2's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.10× lower at baseline in the lines without CELSR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, -1.4); signed map (-3.1, 48.9). **Vector** length 94.1, 27.9% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.7 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +1.6 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.4 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -4.3 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.8 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | -3.8 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.5 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -2.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.2 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | cadherin EGF LAG seven-pass G-type receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,360,834-46,537,620 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ME2, HFMI2, FMI2, CDHF9, ADGRC1 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily C; CELSR cadherins |
| Hallmark sets | HEDGEHOG_SIGNALING, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYQ6](https://www.uniprot.org/uniprotkb/Q9NYQ6) (Cadherin EGF LAG seven-pass G-type receptor 1):

> Receptor that may have an important role in cell/cell signaling during nervous system formation.

**Summary**, from NCBI Gene [9620](https://www.ncbi.nlm.nih.gov/gene/9620):

> The protein encoded by this gene is a member of the flamingo subfamily, part of the cadherin superfamily. The flamingo subfamily consists of nonclassic-type cadherins; a subpopulation that does not interact with catenins. The flamingo cadherins are located at the plasma membrane and have nine cadherin domains, seven epidermal growth factor-like repeats and two laminin A G-type repeats in their ectodomain. They also have seven transmembrane domains, a characteristic unique to this subfamily. It …

**Accessions** — [HGNC:1850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1850) · Entrez [9620](https://www.ncbi.nlm.nih.gov/gene/9620) · UniProt [Q9NYQ6](https://www.uniprot.org/uniprotkb/Q9NYQ6) · Ensembl [ENSG00000075275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075275)

## Data

Gene col 1110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1110); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1110]; `tensor/DDL_lfc|DDL_z.npy` [1110]; `embed/gene_vectors.npy` [1110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1110 or target_col == 1110). Every well: [[CELSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
