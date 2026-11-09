---
symbol: "TAPT1"
type: "gene"
col: 9854
ensembl_id: "ENSG00000169762"
name: "transmembrane anterior posterior transformation 1"
location: "4p15.32"
module: 130
arm: "+"
pooled_cpm: 37.45
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# TAPT1

*transmembrane anterior posterior transformation 1* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +15.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.393× (z -13.9, q 3e-41, down in 38 of 44 measured lines) ⚠ toxic; transcription drop; position correction uncertain. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.562× (z -8.6, q 2e-15, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LNX2]] (+0.72, fdr 7e-06), [[CMC4]] (+0.69, fdr 7e-06), [[TXNDC16]] (+0.69, fdr 7e-06); moves opposite to [[EIPR1]] (-0.65, fdr 7e-06), [[FERMT3]] (-0.63, fdr 1e-05), [[RRP7BP-1]] (-0.62, fdr 9e-06).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DGKG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +15.7 | 0e+00 | 46/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.3 | 2e-27 | 41/48 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +8.8 | 2e-16 | 38/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +7.6 | 5e-12 | 37/48 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 3e-06 | 29/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.2 | 2e-05 | 29/47 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.2 | 2e-05 | 27/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 8e-05 | 27/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.8 | 1e-04 | 29/48 (HT-29, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +4.7 | 1e-04 | 28/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.3 | 9e-04 | 21/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 25/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 21/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.048 | 16/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.053 | 16/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.393×** | -13.9 | 3e-41 | 38/44 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.453×** | -11.3 | 2e-27 | 32/38 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.562×** | -8.6 | 2e-15 | 42/48 (HT-29, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.582×** | -8.0 | 1e-13 | 35/48 (KATO III, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change; position correction uncertain | **0.560×** | -8.0 | 2e-13 | 28/40 (Panc 03.27, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.672×** | -5.9 | 3e-07 | 35/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.676×** | -5.8 | 5e-07 | 28/48 (KATO III, SW480, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.577×** | -4.3 | 0.001 | 26/47 (NCI-H2347, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.603×** | -3.9 | 0.005 | 23/48 (SNU-423, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.606×** | -3.9 | 0.006 | 22/47 (NCI-H1792, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.614×** | -3.8 | 0.008 | 20/44 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.773×** | -3.7 | 0.011 | 20/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.015 | 19/48 (NCI-H2347, SW 1088, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | **0.635×** | -3.5 | 0.017 | 19/48 (NCI-H2347, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.792×** | -3.5 | 0.020 | 15/48 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.051 | 15/48 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.674×** | -3.1 | 0.069 | 19/46 (A498, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.081 | 14/48 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.809×** | -3.0 | 0.082 | 21/48 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 42.7 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -12.8) ⚠ toxic; transcription drop; position correction uncertain |
| [[SW480 (line)]] | alt | 45.5 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0420× (z -32.9) ⚠ toxic; transcription drop; position correction uncertain |
| [[NCI-H2347 (line)]] | alt | 61.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -17.0) ⚠ toxic; transcription drop; position correction uncertain |
| [[CFPAC-1 (line)]] | alt | 63.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -12.5) ⚠ toxic; transcription drop; position correction uncertain |
| [[HT-29 (line)]] | alt | 34.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.271× (z -10.2) |
| [[LoVo (line)]] | wt | 37.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 50.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.4) ⚠ toxic; transcription drop; position correction uncertain |
| [[Panc 03.27 (line)]] | alt | 46.4 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0738× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change; position correction uncertain |
| [[HEC-1-A (line)]] | alt | 40.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -8.5) ⚠ toxic; transcription drop; position correction uncertain |
| [[HOP62 (line)]] | alt | 37.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.3) ⚠ toxic; transcription drop; position correction uncertain · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -9.0) |
| [[PANC-1 (line)]] | alt | 19.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.3) | [[Bortezomib (drug)]] 5 µM 0.0605× (z -13.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 37.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.8) ⚠ toxic; transcription drop; position correction uncertain |
| [[A549 (line)]] | wt | 31.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.3) ⚠ toxic; transcription drop; position correction uncertain |
| [[H4 (line)]] | wt | 56.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 22.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 44.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -13.1) ⚠ toxic; transcription drop; position correction uncertain |
| [[NCI-H1792 (line)]] | alt | 48.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -10.0) ⚠ toxic; transcription drop; position correction uncertain |
| [[SW 900 (line)]] | alt | 81.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -12.6) ⚠ toxic; transcription drop; position correction uncertain |
| [[SW48 (line)]] | wt | 40.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -9.8) ⚠ toxic; transcription drop; position correction uncertain |
| [[A-427 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -10.7) ⚠ toxic; transcription drop; position correction uncertain |
| [[AsPC-1 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0626× (z -19.0) ⚠ toxic; transcription drop; position correction uncertain |
| [[NCI-H460 (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.7) | — |
| [[RKO (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0968× (z -15.8) ⚠ toxic; transcription drop; position correction uncertain |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.0) ⚠ toxic; transcription drop; position correction uncertain |
| [[A-172 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | +0.72 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[CMC4]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[DICER1-AS1]] | +0.68 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SIAH1]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FBXL3]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CHASERR]] | +0.65 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RAF1]] | +0.64 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[KLHDC2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ACOT2]] | +0.63 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIPR1]] | -0.65 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[FERMT3]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.62 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[DFFA]] | -0.62 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[MRPS28]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[C7orf50]] | -0.58 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[TBC1D22A]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PSMD3]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CMIP]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PWWP3A]] | -0.57 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ZNF473]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CLPB]] | -0.56 | -0.57 / -0.60 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKG]] | B | DGKG activity raises TAPT1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without DGKG | 0.018 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TAPT1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.4, -26.1); signed map (25.0, -16.3). **Vector** length 99.6, 26.9% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +15.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.5 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | -3.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane anterior posterior transformation 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:16,160,505-16,227,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90013 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXT6](https://www.uniprot.org/uniprotkb/Q6NXT6) (Transmembrane anterior posterior transformation protein 1 homolog):

> Plays a role in primary cilia formation. May act as a downstream effector of HOXC8 possibly by transducing or transmitting extracellular information required for axial skeletal patterning during development (By similarity). May be involved in cartilage and bone development (By similarity). May play a role in the differentiation of cranial neural crest cells (By similarity).; (Microbial infection) In case of infection, may act as a fusion receptor for cytomegalovirus (HCMV) strain AD169.

**Summary**, from NCBI Gene [202018](https://www.ncbi.nlm.nih.gov/gene/202018):

> This gene encodes a highly conserved protein that localizes to the centrosome and/or ciliary basal body. Mutations in this gene disrupt Golgi morphology and trafficking and normal primary cilium formation and these mutations are congenitally manifested by severe undermineralization of the intra-uterine skeleton. A mutation in the mouse ortholog of this gene results in homeotic, posterior-to-anterior transformations of the axial skeleton which are similar to the phenotype of mouse homeobox C8 …

**Accessions** — [HGNC:26887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26887) · Entrez [202018](https://www.ncbi.nlm.nih.gov/gene/202018) · UniProt [Q6NXT6](https://www.uniprot.org/uniprotkb/Q6NXT6) · Ensembl [ENSG00000169762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169762)

## Data

Gene col 9854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9854); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9854]; `tensor/DDL_lfc|DDL_z.npy` [9854]; `embed/gene_vectors.npy` [9854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9854 or target_col == 9854). Every well: [[TAPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
