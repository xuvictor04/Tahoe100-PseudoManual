---
symbol: "BACH2"
type: "gene"
col: 3331
ensembl_id: "ENSG00000112182"
name: "BACH transcriptional regulator 2"
location: "6q15"
module: 206
arm: "+"
pooled_cpm: 46.81
n_lines_expressing: 43
n_dd_up: 44
n_dd_down: 13
n_dd_up_clean: 40
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# BACH2

*BACH transcriptional regulator 2* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.85× (z +35.2, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.394× (z -17.3, q 0e+00, down in 36 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.559× (z -7.7, q 4e-12, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JMJD1C]] (+0.61, fdr 1e-05), [[IL18]] (+0.57, fdr 1e-05), [[RNF223]] (+0.55, fdr 1e-04); moves opposite to [[ADPGK]] (-0.47, fdr 3e-05), [[MLEC]] (-0.47, fdr 4e-05), [[SNHG30]] (-0.46, fdr 3e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PGBD5]] → it (grade B ⚠); 4 go from it, the strongest it → [[DAAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.85×** | +35.2 | 0e+00 | 39/41 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.60×** | +22.8 | 0e+00 | 38/41 (LS 180, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.34×** | +22.2 | 0e+00 | 38/41 (SW480, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.89×** | +19.6 | 0e+00 | 36/41 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +18.6 | 0e+00 | 33/41 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +17.9 | 0e+00 | 34/41 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +17.1 | 0e+00 | 33/41 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +16.3 | 0e+00 | 30/41 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +12.0 | 2e-31 | 30/42 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.75×** | +9.9 | 2e-21 | 29/40 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +9.8 | 5e-21 | 27/41 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +9.0 | 1e-17 | 27/42 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.58×** | +8.5 | 1e-15 | 28/41 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.58×** | +8.1 | 2e-14 | 23/40 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.54×** | +7.9 | 9e-14 | 24/40 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.8 | 2e-13 | 18/42 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.394×** | -17.3 | 0e+00 | 36/41 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.559×** | -7.7 | 4e-12 | 25/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.349×** | -6.5 | 2e-08 | 23/41 (NCI-H1792, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -6.4 | 2e-08 | 20/34 (SW48, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.413×** | -5.4 | 7e-06 | 19/40 (SW48, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.750×** | -5.4 | 8e-06 | 22/38 (SNU-1, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.747×** | -5.1 | 2e-05 | 17/41 (SW48, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.493×** | -4.3 | 1e-03 | 13/41 (SW48, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.725×** | -4.3 | 0.001 | 17/42 (SW48, SW 1271, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.504×** | -4.2 | 0.002 | 16/39 (SW48, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.805×** | -3.7 | 0.010 | 18/36 (Panc 03.27, NCI-H661, …) | all doses, stronger at high dose | composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.020 | 11/41 (SW48, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~1% of this change | 0.839× | -3.3 | 0.046 | 17/38 (NCI-H661, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.589×** | -3.2 | 0.047 | 11/41 (SW48, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.842× | -3.1 | 0.078 | 13/40 (BT-474, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.080 | 11/41 (LoVo, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.0 | 21 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +16.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.153× (z -16.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 23.3 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +22.1) | — |
| [[LoVo (line)]] | wt | 60.1 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.6) | — |
| [[SNU-1 (line)]] | wt | 311 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0900× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SW 900 (line)]] | alt | 30.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +18.5) | — |
| [[BT-474 (line)]] | alt | 81.0 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.225× (z -10.0) |
| [[C-33 A (line)]] | alt | 407 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -17.3) |
| [[HOP62 (line)]] | alt | 21.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +18.3) | — |
| [[J82 (line)]] | alt | 25.2 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +17.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -10.5) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 190 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0955× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.8) |
| [[SW480 (line)]] | alt | 17.5 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 5.88× (z +16.8) | — |
| [[SHP-77 (line)]] | alt | 135 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 200 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -18.8) |
| [[A-172 (line)]] | wt | 14.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +21.3) | — |
| [[NCI-H1792 (line)]] | alt | 49.5 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 666 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0817× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -11.0) |
| [[PANC-1 (line)]] | alt | 21.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.03× (z +10.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -13.1) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 234 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0382× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -8.5) |
| [[A498 (line)]] | wt | 16.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +16.0) | — |
| [[A549 (line)]] | wt | 18.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +15.4) | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +16.3) | — |
| [[SNU-423 (line)]] | alt | 87.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 35.6 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.44× (z +10.5) | — |
| [[H4 (line)]] | wt | 15.6 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 14.5× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 75.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.4) |
| [[A-427 (line)]] | wt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +15.9) | — |
| [[COLO 205 (line)]] | alt | 18.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.2× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 39.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 11.6× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 64.5 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.66× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -8.8) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.64× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMJD1C]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[IL18]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RNF223]] | +0.55 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SH3GL2]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PARD6B]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TBC1D9]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[SNX9]] | +0.53 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[CLIP2]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[KLF6]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PIK3CD]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[IGF2BP2]] | +0.52 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[FOXO3]] | +0.51 | +0.32 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPGK]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MLEC]] | -0.47 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SNHG30]] | -0.46 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[FAM53B]] ⚠ | -0.46 | -0.30 / -0.47 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SNRNP40]] | -0.45 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[ANAPC10]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PMS2]] | -0.44 | -0.31 / -0.40 | both halves | 2e-04 | pathway: Affinity selection of immunoglobulins |
| [[ZUP1]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ZCCHC4]] | -0.44 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[TIMM21]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGBD5]] | B | PGBD5 activity raises BACH2's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without PGBD5 | 0.030 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[MTOR]] | B | MTOR activity lowers BACH2's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 7.6% of all compounds | 0.059 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RUNDC3B]] | B | RUNDC3B activity raises BACH2's level | lines that do not express RUNDC3B (8) vs lines expressing it (42) | 3.55× lower at baseline in the lines without RUNDC3B | 0.087 | ⚠ within organs, on part of the lines; also absent: STC2, FAM171B, RTKN2; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAAM1]] | B | BACH2 activity raises DAAM1's level | lines that do not express BACH2 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without BACH2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | B | BACH2 activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express BACH2 (7) vs lines expressing it (41) | the lines without BACH2: 0.83× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |
| [[IER5]] | B | BACH2 activity raises IER5's level | lines that do not express BACH2 (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without BACH2 | 0.080 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |
| [[GRHL1]] | B | BACH2 activity raises GRHL1's level | lines that do not express BACH2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without BACH2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.1, 11.3); signed map (1.6, 22.4). **Vector** length 116, 31.8% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.9 | +22.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.0 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +17.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +22.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +19.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.3 | +9.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +9.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.3 | +7.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.1 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -17.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.5 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | -3.2 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | BACH transcriptional regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,926,528-90,296,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BTBD25 |
| Gene groups (HGNC) | BTB domain containing; BACH transcriptional regulator family |
| Reactome | 4 pathways, smallest: Somatic hypermutation of immunoglobulin genes; Affinity selection of immunoglobulins; Immunoglobulin maturation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYV9](https://www.uniprot.org/uniprotkb/Q9BYV9) (Transcription regulator protein BACH2):

> Transcriptional regulator that acts as a repressor or activator (By similarity). Binds to Maf recognition elements (MARE) (By similarity). Plays an important role in coordinating transcription activation and repression by MAFK (By similarity). Induces apoptosis in response to oxidative stress through repression of the antiapoptotic factor HMOX1. Positively regulates the nuclear import of actin (By similarity). Is a key regulator of adaptive immunity, crucial for the maintenance of regulatory …

**Summary**, from NCBI Gene [60468](https://www.ncbi.nlm.nih.gov/gene/60468):

> Enables sequence-specific double-stranded DNA binding activity. Involved in primary adaptive immune response involving T cells and B cells. Located in cytosol and nucleoplasm. Implicated in immunodeficiency 60. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14078) · Entrez [60468](https://www.ncbi.nlm.nih.gov/gene/60468) · UniProt [Q9BYV9](https://www.uniprot.org/uniprotkb/Q9BYV9) · Ensembl [ENSG00000112182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112182)

## Data

Gene col 3331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3331); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3331]; `tensor/DDL_lfc|DDL_z.npy` [3331]; `embed/gene_vectors.npy` [3331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3331 or target_col == 3331). Every well: [[BACH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BACH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
