---
symbol: "SQLE"
type: "gene"
col: 2473
ensembl_id: "ENSG00000104549"
name: "squalene epoxidase"
location: "8q24.13"
module: 86
arm: "+"
pooled_cpm: 77.66
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SQLE

*squalene epoxidase* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 2.22× (z +12.7, q 2e-34, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.663× (z -6.5, q 3e-08, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVD]] (+0.83, fdr 7e-06), [[HMGCR]] (+0.82, fdr 7e-06), [[MSMO1]] (+0.79, fdr 7e-06); moves opposite to [[VPS52]] (-0.55, fdr 1e-04), [[DECR1]] (-0.53, fdr 1e-04), [[SCRN1]] (-0.53, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **2.22×** | +12.7 | 2e-34 | 45/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **2.08×** | +11.7 | 4e-29 | 44/47 (HOP62, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +9.2 | 9e-18 | 41/46 (J82, C-33 A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +6.7 | 3e-09 | 36/47 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +5.9 | 4e-07 | 34/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.60×** | +5.1 | 3e-05 | 35/47 (AsPC-1, HOP62, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.57×** | +5.1 | 3e-05 | 35/47 (HT-29, HOP62, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +4.6 | 3e-04 | 32/48 (C32, HOP62, …) | top dose only | plate-row cell shift |
| [[Terfenadine (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 34/47 (HT-29, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 9e-04 | 30/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +4.3 | 9e-04 | 33/47 (C32, HOP62, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 30/47 (HOP62, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.7 | 0.008 | 31/47 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.008 | 27/46 (NCI-H2347, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.023 | 24/47 (PANC-1, LS 180, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.047 | 22/47 (SW1417, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Berbamine (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.060 | 22/47 (HT-29, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -6.5 | 3e-08 | 33/47 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -6.2 | 2e-07 | 30/42 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.623×** | -5.3 | 2e-05 | 32/47 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.760×** | -4.4 | 0.002 | 27/48 (KATO III, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -4.4 | 0.002 | 32/47 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.773×** | -4.1 | 0.004 | 28/47 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -3.7 | 0.018 | 22/47 (BT-474, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.704×** | -3.6 | 0.024 | 23/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.712×** | -3.5 | 0.026 | 25/46 (HS-578T, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.733×** | -3.2 | 0.067 | 21/44 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.743×** | -3.2 | 0.067 | 20/47 (BT-474, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.814×** | -3.2 | 0.068 | 18/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.068 | 23/47 (HS-578T, RKO, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.088 | 22/47 (LoVo, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 125 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -12.9) |
| [[HS-578T (line)]] | alt | 334 | 2 | 6 (3 ⚠) | [[Berbamine (drug)]] 5 µM 2.36× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -12.8) |
| [[A498 (line)]] | wt | 198 | 2 | 5 (3 ⚠) | [[Berbamine (drug)]] 5 µM 2.09× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -16.4) |
| [[HOP62 (line)]] | alt | 64.7 | 3 (1 ⚠) | 2 | [[Cepharanthine (drug)]] 5 µM 3.42× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.5) |
| [[Hs 766T (line)]] | wt | 381 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.4) |
| [[LS 180 (line)]] | wt | 25.5 | 2 | 2 (1 ⚠) | [[Berbamine (drug)]] 5 µM 4.98× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -8.5) |
| [[SW 900 (line)]] | alt | 56.9 | 2 | 2 (2 ⚠) | [[Berbamine (drug)]] 5 µM 2.72× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 68.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 54.8 | 2 | 1 | [[Berbamine (drug)]] 5 µM 3.61× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.4) |
| [[C-33 A (line)]] | alt | 58.5 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 3.74× (z +12.4) | — |
| [[J82 (line)]] | alt | 81.4 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.80× (z +11.7) ⚠ toxic · without an alert: [[Cepharanthine (drug)]] 5 µM 2.07× (z +9.3) | — |
| [[LoVo (line)]] | wt | 32.5 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 5.70× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 39.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.97× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 50.3 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.68× (z +9.4) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 3.97× (z +8.7) | — |
| [[A549 (line)]] | wt | 63.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.91× (z +11.3) | — |
| [[C32 (line)]] | wt | 45.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.19× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 40.2 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.33× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 143 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.29× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 80.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.69× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 34.8 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.55× (z +9.4) | — |
| [[RKO (line)]] | wt | 162 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.3) |
| [[SNU-423 (line)]] | alt | 29.0 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.17× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 53.7 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.57× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 70.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 21.1 | 1 | 0 | [[Berbamine (drug)]] 5 µM 3.20× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.69× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 83.5 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[NCI-H596 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.131× (z -10.6) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 94.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 78.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.43× (z +9.3) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -13.0) |
| [[A-427 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVD]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 906 |
| [[HMGCR]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 973 |
| [[MSMO1]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 992 |
| [[FDFT1]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 999 |
| [[EBP]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 697 |
| [[INSIG1]] | +0.75 | +0.77 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 773 |
| [[SREBF2]] | +0.72 | +0.72 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 892 |
| [[FDPS]] | +0.72 | +0.79 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 942 |
| [[ACSS2]] | +0.71 | +0.78 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 604 |
| [[MVK]] | +0.71 | +0.67 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 859 |
| [[IDI1]] | +0.70 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 957 |
| [[DHCR7]] | +0.70 | +0.77 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 983 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | -0.55 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DECR1]] | -0.53 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[SCRN1]] | -0.53 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[C11orf58]] | -0.53 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[DDX6]] | -0.53 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[MED12]] | -0.53 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[DDX39B]] | -0.51 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MTHFSD]] | -0.51 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[PSME3IP1]] | -0.51 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ZMYND11]] | -0.51 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[CASD1]] | -0.51 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ARFGAP2]] | -0.50 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -48.8); signed map (-53.1, 32.4). **Vector** length 152, 52.3% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.62 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.60 to 7); *androgen response* (hallmark, mean cos +0.59 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +9.3 | +11.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.4 | +12.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.5 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.4 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.1 | +4.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.4 | +5.1 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +4.9 | +4.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +4.9 | +5.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.1 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.7 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | squalene epoxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:124,998,497-125,022,283 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Oxygenases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, MTORC1_SIGNALING, G2M_CHECKPOINT |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14534](https://www.uniprot.org/uniprotkb/Q14534) (Squalene monooxygenase):

> Catalyzes the stereospecific oxidation of squalene to (S)-2,3-epoxysqualene, and is considered to be a rate-limiting enzyme in steroid biosynthesis.

**Summary**, from NCBI Gene [6713](https://www.ncbi.nlm.nih.gov/gene/6713):

> Enables FAD binding activity and squalene monooxygenase activity. Involved in cholesterol biosynthetic process; lipid droplet formation; and regulation of cell population proliferation. Located in membrane. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11279) · Entrez [6713](https://www.ncbi.nlm.nih.gov/gene/6713) · UniProt [Q14534](https://www.uniprot.org/uniprotkb/Q14534) · Ensembl [ENSG00000104549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104549)

## Data

Gene col 2473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2473); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2473]; `tensor/DDL_lfc|DDL_z.npy` [2473]; `embed/gene_vectors.npy` [2473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2473 or target_col == 2473). Every well: [[SQLE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SQLE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
