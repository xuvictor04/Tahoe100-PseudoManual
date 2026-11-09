---
symbol: "FAM117B"
type: "gene"
col: 6176
ensembl_id: "ENSG00000138439"
name: "family with sequence similarity 117 member B"
location: "2q33.2"
module: 134
arm: "+"
pooled_cpm: 85.47
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 38
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# FAM117B

*family with sequence similarity 117 member B* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +6.8, q 8e-09, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.198× (z -30.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1958]] (+0.74, fdr 7e-06), [[SLC2A3]] (+0.71, fdr 1e-05), [[BNIP3L]] (+0.71, fdr 7e-06); moves opposite to [[CPLANE1]] (-0.63, fdr 7e-06), [[SLC9A8]] (-0.61, fdr 1e-05), [[ITPA]] (-0.58, fdr 4e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARMCX4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.8 | 8e-09 | 30/48 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.77×** | +5.8 | 2e-06 | 29/48 (HOP62, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.6 | 3e-06 | 26/48 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 0.003 | 20/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.003 | 21/49 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +3.6 | 0.026 | 21/49 (SW 900, HS-578T, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +3.4 | 0.064 | 16/48 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.099 | 9/49 (J82, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.198×** | -30.3 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.356×** | -28.3 | 0e+00 | 44/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.273×** | -25.2 | 0e+00 | 47/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.309×** | -21.9 | 0e+00 | 42/44 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.407×** | -17.4 | 0e+00 | 46/49 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -14.2 | 8e-44 | 41/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.499×** | -13.5 | 2e-39 | 45/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.528×** | -12.4 | 3e-33 | 34/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.548×** | -11.2 | 3e-27 | 38/47 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -11.2 | 3e-27 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.560×** | -10.4 | 1e-23 | 34/45 (AN3 CA, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -9.4 | 4e-19 | 37/47 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.402×** | -9.2 | 1e-18 | 42/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.424×** | -8.7 | 1e-16 | 41/48 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.460×** | -7.9 | 1e-13 | 36/48 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -7.8 | 2e-13 | 35/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.662×** | -7.7 | 5e-13 | 35/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -7.6 | 8e-13 | 31/50 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.496×** | -7.1 | 3e-11 | 35/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -6.5 | 2e-09 | 30/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[EX229 (drug)]] 5 µM |  | **0.554×** | -6.0 | 5e-08 | 29/48 (PANC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.754×** | -5.5 | 1e-06 | 27/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 277 | 1 | 16 (10 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -22.6) |
| [[PANC-1 (line)]] | alt | 63.8 | 0 | 14 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -26.1) |
| [[NCI-H460 (line)]] | wt | 85.9 | 0 | 13 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0961× (z -24.4) |
| [[SW48 (line)]] | wt | 148 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -15.2) |
| [[SW480 (line)]] | alt | 74.7 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -21.3) |
| [[CFPAC-1 (line)]] | alt | 161 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -23.3) |
| [[HT-29 (line)]] | alt | 102 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0892× (z -19.7) |
| [[MIA PaCa-2 (line)]] | alt | 99.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 74.8 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.68× (z +8.6) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.0829× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -19.6) |
| [[NCI-H2030 (line)]] | alt | 65.9 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -20.2) |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0858× (z -25.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.143× (z -20.1) |
| [[C-33 A (line)]] | alt | 131 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0820× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 151 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.1) |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.179× (z -16.1) |
| [[SNU-1 (line)]] | wt | 100.0 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0699× (z -18.2) |
| [[A-427 (line)]] | wt | 96.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -27.1) |
| [[AsPC-1 (line)]] | alt | 88.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.7) |
| [[HEC-1-A (line)]] | alt | 74.8 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.367× (z -11.2) |
| [[RKO (line)]] | wt | 46.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.1) |
| [[A-172 (line)]] | wt | 55.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.9) |
| [[A498 (line)]] | wt | 49.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.230× (z -16.5) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.310× (z -13.1) |
| [[AN3 CA (line)]] | alt | 107 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0681× (z -16.3) |
| [[HCT15 (line)]] | alt | 228 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0813× (z -13.9) |
| [[HOP62 (line)]] | alt | 103 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.9) |
| [[J82 (line)]] | alt | 88.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.3) |
| [[LS 180 (line)]] | wt | 104 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -15.1) |
| [[SNU-423 (line)]] | alt | 74.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -21.3) |
| [[A549 (line)]] | wt | 72.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -20.8) |
| [[HS-578T (line)]] | alt | 52.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -12.1) |
| [[KATO III (line)]] | alt | 36.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.6) |
| [[LoVo (line)]] | wt | 69.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 32.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 50.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -11.6) |
| [[SW 900 (line)]] | alt | 55.1 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -13.8) |
| [[COLO 205 (line)]] | alt | 73.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -13.2) |
| [[H4 (line)]] | wt | 109 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.156× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 69.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 78.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.348× (z -11.6) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.8) |
| [[CHP-212 (line)]] | wt | 97.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.8) |
| [[Hs 766T (line)]] | wt | 32.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -10.1) |
| [[NCI-H2122 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[SLC2A3]] | +0.71 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[BNIP3L]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SNX25]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.70 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[RIMKLA]] | +0.70 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PDXP]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[FBXO33]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MXI1]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RERE]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPLANE1]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SLC9A8]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ITPA]] | -0.58 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.58 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[CHMP3]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CC2D1B]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[BRPF3]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RC3H2]] | -0.55 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[VPS35L]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ERMAP]] | -0.54 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[PPP3CB-AS1]] | -0.54 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ARFGAP2]] | -0.54 | -0.56 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX4]] | B | ARMCX4 activity weakens FAM117B's drug response | lines that do not express ARMCX4 (18) vs lines expressing it (31) | the lines without ARMCX4 respond 1.27× as strongly (z diff -1.28); strongest at Digitoxin 5 µM: 0.42x vs 0.63x (z diff -3.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FAM117B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FAM117B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAML3]] | B | MAML3 activity lowers FAM117B's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without MAML3 | 0.095 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.808). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.9, -12.9); signed map (-35.1, 27.5). **Vector** length 139, 48.1% of its response variance represented; |z| ≥ 3 in 1,663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +8.2 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.9 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.5 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +6.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +5.3 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -0.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.8 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.4 | -30.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -25.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -13.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.8 | -9.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.3 | -8.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 117 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:202,634,969-202,769,757 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38771; previously ALS2CR13 |
| Matched by | ensembl_id |

UniProt [Q6P1L5](https://www.uniprot.org/uniprotkb/Q6P1L5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:14440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14440) · Entrez [150864](https://www.ncbi.nlm.nih.gov/gene/150864) · UniProt [Q6P1L5](https://www.uniprot.org/uniprotkb/Q6P1L5) · Ensembl [ENSG00000138439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138439)

## Data

Gene col 6176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6176); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6176]; `tensor/DDL_lfc|DDL_z.npy` [6176]; `embed/gene_vectors.npy` [6176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6176 or target_col == 6176). Every well: [[FAM117B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM117B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
